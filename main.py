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


template = """

Current conversation:
{history}
user: {input}
AI:"""


llm = Ollama(model="llama2", temperature=0, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))

template = """
[INST] <<SYS>>
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, please don't share false information.
<</SYS>>
here is the chat history
{chat_history}

{prompt} [/INST]
"""

prompt = PromptTemplate(
    input_variables=["chat_history", "prompt"],
    template=template
)

memory = ConversationBufferMemory(memory_key="chat_history",    
                                  k=10,
                                  return_messages=True)

llm_chain = LLMChain(llm=llm, prompt=prompt, verbose=False,  memory=memory)

while True:

    query = input("\nQuery: ")
    if query == "exit":
        break
    if query.strip() == "":
        continue
    
    output=llm_chain.predict(prompt=query)


    # print(conversation.prompt.template)
    # result = llm.invoke(query)
    # i am lihan, studying in china