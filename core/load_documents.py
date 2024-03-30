from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader

def load_web(url):
    loader = WebBaseLoader(url)
    doc = loader.load()
    return doc

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    doc = loader.load()
    return doc

