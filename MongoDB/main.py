# Import necessary libraries and dependencies
import os
from dotenv import load_dotenv
import time
from sentence_transformers import SentenceTransformer
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pymongo import MongoClient
from pymongo.operations import SearchIndexModel

# Load environment variables from .env file
load_dotenv()

# Get required environment variable.
mongodb_connection_string = os.getenv('MONGODB_CONNECTION_STRING')
gemini_api_keys = os.getenv('GEMINI_API_KEYS')

if not mongodb_connection_string and not gemini_api_keys:
  print('MongoDB Connection String and/or Gemini API Keys not provided.')

# Initiate required modals.
model = SentenceTransformer("nomic-ai/nomic-embed-text-v1", trust_remote_code=True)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", google_api_key=gemini_api_keys)



# Helper functions.

# Load the PDF
def get_data_from_pdf(pdf_url):
  loader = PyPDFLoader(pdf_url)
  return loader.load()

def split_text_into_chunks(data, chunk_size=400, chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  return text_splitter.split_documents(data)

# Function to convert string into embeddings.
def convert_text_to_embeddings(data, model):
    # Initiate the embedding model.
    embedding = model.encode(data)
    return embedding.tolist()

def get_mongodb_collection(mongodb_connection_string, db_name, collection_name):
    client = MongoClient(mongodb_connection_string)
    return client[db_name][collection_name]

def is_index_ready(index_name):
  """
  MongoDB does not make the vector search index immediately usable after creation.
  This block is a readiness check loop to wait until MongoDB finishes setting up the index.
  Without this check, any vector search query would likely fail or return empty results.
  """
  predicate=None

  if predicate is None:
    predicate = lambda index: index.get("queryable") is True

  while True:
    indices = list(collection.list_search_indexes(index_name))
    if len(indices) and predicate(indices[0]):
      break
    time.sleep(5)

def create_cosine_search_index(collection, index_name):
   # Create the search index
  search_index_model = SearchIndexModel(
    definition = {
      "fields": [
        {
          "type": "vector",
          "numDimensions": 768,
          "path": "embedding",
          "similarity": "cosine"
        }
      ]
    },
    name = index_name,
    type = "vectorSearch"
  )

  collection.create_search_index(model=search_index_model)

  is_index_ready(index_name)

# Define a function to run vector search queries
def get_relevant_chunks(collection, query, chunks_required=5):
  query_embedding = convert_text_to_embeddings(query, model)
  pipeline = [
    {
      "$vectorSearch": {
        "index": "vector_index",
        "queryVector": query_embedding,
        "path": "embedding",
        "exact": True,
        "limit": chunks_required
      }
    },
    {
      "$project": {
        "_id": 0,
        "text": 1
      }
    }
  ]

  results = list(collection.aggregate(pipeline))

  return " ".join([doc["text"] for doc in results])

def generate_response(prompt, relevant_chunk_of_data, llm):
  # Create a prompt template
  prompt_template = PromptTemplate(
    input_variables=["prompt", "relevant_chunk_of_data"], 
    template= """
      Use the following pieces of context to answer the question at the end.

      Context: {relevant_chunk_of_data}

      User's Question: {prompt}
      """
    )

  # Chain the template and instance
  chain = prompt_template | llm

  # Invoke the chain by passing the input variables of prompt
  response = chain.invoke({
    "prompt":prompt,
    "relevant_chunk_of_data": relevant_chunk_of_data
  })

  # Return the response
  return response.content



# RAG

# Get data from pdf.
print("Fetch Data: Start")
data = get_data_from_pdf("https://investors.mongodb.com/node/12236/pdf")
print("Fetch Data: Complete")

# Split the data into chunks.
print("Text Chunking: Start")
documents = split_text_into_chunks(data, 400, 20)
print("Text Chunking: Done")

# Structure the splited chunks with text and embeddings.
docs_to_insert = [{
    "text": doc.page_content,
    "embedding": convert_text_to_embeddings(doc.page_content, model)
} for doc in documents]

# Get MongoDB collection.
print("Get Collection: Start")
collection = get_mongodb_collection(mongodb_connection_string, "rag_db", "embeddings")   
print("Get Collection: Done")

# Insert splited chunks into the collection.
print("Insert Documents: Start")
collection.insert_many(docs_to_insert)
print("Insert Documents: Done")

# Create a vector index in the collection.
print("Create Index: Start")
create_cosine_search_index(collection, "vector_index")
print("Create Index: Done")

# Define the query.
query = "What are MongoDB's latest AI announcements?"

# Get 5 relevant chunks of stored data based on the query.
print("Get Relevant Data: Start")
relevant_chunks = get_relevant_chunks(collection, query, 5)
print("Get Relevant Data: Done")

# Get the generated response by passing the query and relevant chunk of data to Gemini.
generated_response = generate_response(query, relevant_chunks, llm)

print(generated_response)