from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community import embeddings
from langchain.vectorstores.chroma import Chroma
from .load_documents import load_web, load_pdf

ChromaDB_PATH = "./chromadb"

def create_text_splitter(chunk_size: int = 1000, chunk_overlap: int = 200)-> RecursiveCharacterTextSplitter:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        add_start_index=True)
    return splitter

def create_ollama_embedding():
    embedding_model = embeddings.OllamaEmbeddings(
        model="nomic-embed-text"
    )
    return embedding_model

def create_vectorestore(embeddings_model, all_split):
    vectorestore = Chroma.from_documents(
        documents=all_split,
        embedding=embeddings_model,
        persist_directory=ChromaDB_PATH
    )
    return vectorestore


def create_vectorestore_webpage(url):
    doc = load_web(url)
    text_splitter = create_text_splitter()
    all_split = text_splitter.split_documents(doc)
    embeddings_model = create_ollama_embedding()
    vectorestore = create_vectorestore(embeddings_model, all_split)
    return vectorestore


def create_vectorestore_pdf(pdf):
    doc = load_pdf(pdf)
    text_splitter = create_text_splitter()
    all_split = text_splitter.split_documents(doc)
    embeddings_model = create_ollama_embedding()
    vectorestore = create_vectorestore(embeddings_model, all_split)
    return vectorestore


if __name__ == "__main__":
    url = "https://medium.com/neo4j/json-based-agents-with-ollama-langchain-9cf9ab3c84ef"
    vectorestore = create_vectorestore_webpage(url)
    ret = vectorestore.as_retriever(
        search_type = "similarity",
        search_kwargs = {"k": 6}
    )
    print(ret.get_relevant_documents("what is JSON-based Prompt "))
    
