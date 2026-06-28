from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from langchain_community.vectorstores import FAISS

#load api key from env
load_dotenv()

#load pdf 
loader = PyPDFLoader("data/dsa.pdf")
documents = loader.load()

#split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap =100
)

chunks = text_splitter.split_documents(documents)
chunks = chunks[:100]
#create embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview"
)

#create faiss vector databse IMP
vector_store = FAISS.from_documents(chunks,embeddings)

#save it locally
vector_store.save_local("faiss_index")
print("FAISS database careated successfully!")