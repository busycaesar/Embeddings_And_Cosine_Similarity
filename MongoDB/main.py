import os
from sentence_transformers import SentenceTransformer
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pymongo import MongoClient
from pymongo.operations import SearchIndexModel
import time
import pprint
from dotenv import load_dotenv

load_dotenv()
