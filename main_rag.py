from langchain_community.document_loaders import OnlinePDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.chains import ConversationChain, LLMChain
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from core.create_llm_model import create_ollama_model
from core.create_prompt import create_simple_prompt, create_retrieval_prompt, template_retrieval
from core.create_chains import create_retrieval_chain
from core.create_memory import create_conversation_buffer_memory, create_conversation_summary_memory
from core.create_vectorstore import create_vectorestore_webpage, create_vectorestore_pdf

def build_url_rag_chain(url):
    llm = create_ollama_model()
    prompt = create_simple_prompt()
    memory = create_conversation_buffer_memory()
    retriever = create_vectorestore_webpage(url).as_retriever(
        search_type = "similarity",
        search_kwargs = {"k": 4})
    chain = create_retrieval_chain(retriever=retriever, llm=llm, prompt=prompt, memory=memory)
    return chain


def build_pdf_rag_chain(pdf_file):
    llm = create_ollama_model()
    prompt = create_retrieval_prompt(template_retrieval)
    global memory
    memory = create_conversation_buffer_memory()
    retriever = create_vectorestore_pdf(pdf_file).as_retriever(
        search_type = "similarity",
        search_kwargs = {"k": 4})
    chain = create_retrieval_chain(retriever=retriever, llm=llm, prompt=prompt, memory=memory)
    return chain
# Now you are a chemistry phd student assisting with battery research. 
# research focussing on developing new anode materials for sodium-ion batteries. 
# we have to write a master thesis on this topic.

def main():
    pdf_file = "/home/liangdao_hanli/Downloads/EI_2021_art00014_Ashok-Dahal.pdf"
    chain = build_pdf_rag_chain(pdf_file)

    while True:

        input_query = input("\nYou: ")
        if input_query == "exit":
            break
        if input_query.strip() == "":
            continue
        
        output=chain.invoke(input_query)
        print(" ")

if __name__ == "__main__":
    main()


    # i am lihan, studying at TUB in Germany
    # hi do you know anode materials for sodium-lon Battery