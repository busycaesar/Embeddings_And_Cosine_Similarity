import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_community import BigQueryVectorStore
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()

# Get required environment variable.
GEMINI_API_KEYS = os.getenv('GEMINI_API_KEYS')
PROJECT_ID = os.getenv('PROJECT_ID')
DATASET = os.getenv('DATASET')
TABLE = os.getenv('TABLE')
REGION = os.getenv('REGION')

class RAG:
    def __init__(self, vector_db, llm):
        self.vector_db = vector_db
        self.llm = llm
   
    def get_data_from_pdf(self, pdf_url):
        loader = PyPDFLoader(pdf_url)
        return loader.load()

    def split_text_into_chunks(self, data, chunk_size=400, chunk_overlap=20):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        return text_splitter.split_documents(data)

    def store_chunks_into_bigquery(self, chunks):
        self.vector_db.add_documents(chunks)

    def fetch_relevant_chunk(self, user_query):
        retrieved_docs = self.vector_db.as_retriever().invoke(user_query)

        return " ".join([doc.page_content for doc in retrieved_docs])

    def generate_response(self, prompt, relevant_chunk_of_data):
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
        chain = prompt_template | self.llm

        # Invoke the chain by passing the input variables of prompt
        response = chain.invoke({
          "prompt":prompt,
          "relevant_chunk_of_data": relevant_chunk_of_data
        })

        # Return the response
        return response.content
    
# Required Models.
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GEMINI_API_KEYS)

bq_vector_store = BigQueryVectorStore(
    project_id=PROJECT_ID,
    dataset_name=DATASET,
    table_name=TABLE,
    location=REGION,
    embedding=embedding_model
)
    
rag_big_query = RAG(bq_vector_store, llm)

print("Start    Get data from pdf")
documents = rag_big_query.get_data_from_pdf("https://investors.mongodb.com/node/12236/pdf")
print("End      Get data from pdf")

print("Start    Split text into chunks")
chunks = rag_big_query.split_text_into_chunks(documents)
print("End      Split text into chunks")

print("Start    store data into vector db")
rag_big_query.store_chunks_into_bigquery(chunks)
print("End      store data into vector db")

query = "What is the main topic of the document?"

print("Start    get relevant data")
retrieved_docs = rag_big_query.fetch_relevant_chunk(query)
print("End      get relevant data")

print("Start    generate response")
response = rag_big_query.generate_response(query, retrieved_docs)
print("End      generate response")

print(response)
