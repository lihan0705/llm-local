from langchain_community.document_loaders import OnlinePDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA
from langchain.chains import ConversationChain, LLMChain
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory



llm = Ollama(model="gemma:7b", temperature=0.1, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
# Now you are a chemistry phd student assisting with battery research. 
# research focussing on developing new anode materials for sodium-ion batteries. 
# we have to write a master thesis on this topic.

def main():
    while True:

        input_query = input("\nprompt: ")
        if input_query == "exit":
            break
        if input_query.strip() == "":
            continue
        
        output=llm.invoke(input=input_query)

if __name__ == "__main__":
    main()


    # i am lihan, studying at TUB in Germany
    # hi do you know anode materials for sodium-lon Battery