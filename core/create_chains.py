from langchain.chains import LLMChain, ConversationChain, RetrievalQA

def create_simple_chain(llm, prompt, memory):
    return LLMChain(prompt=prompt, 
                    llm=llm, 
                    memory=memory, 
                    verbose=False)

def create_conversation_chain(llm, memory):
    return ConversationChain(
                    llm=llm, 
                    memory=memory, 
                    verbose=False)

def create_retrieval_chain(retriever, prompt, llm, memory):
    return RetrievalQA.from_chain_type(
                    llm=llm,
                    retriever=retriever,
                    memory=memory, 
                    chain_type_kwargs={'prompt': prompt})