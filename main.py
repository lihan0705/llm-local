from langchain_community.document_loaders import OnlinePDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.chains import ConversationChain, LLMChain
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from core.create_llm_model import create_ollama_model
from core.create_prompt import create_simple_prompt
from core.create_chains import create_simple_chain
from core.create_memory import create_conversation_buffer_memory

def build_chain():
    llm = create_ollama_model()
    prompt = create_simple_prompt()
    memory = create_conversation_buffer_memory()
    chain = create_simple_chain(llm=llm, prompt=prompt, memory=memory)
    return chain
# Now you are a chemistry phd student assisting with battery research. 
# research focussing on developing new anode materials for sodium-ion batteries. 
# we have to write a master thesis on this topic.

def main():

    chain = build_chain()

    while True:

        input_query = input("\nYou: ")
        if input_query == "exit":
            break
        if input_query.strip() == "":
            continue
        
        output=chain.invoke(input=input_query)
        print(" ")

if __name__ == "__main__":
    main()


    # i am lihan, studying at TUB in Germany
    # hi do you know anode materials for sodium-lon Battery