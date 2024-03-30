from langchain.chains import LLMChain, ConversationChain, RetrievalQA, ConversationalRetrievalChain

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
    return ConversationalRetrievalChain.from_llm(
                    llm=llm,
                    retriever=retriever,
                    memory=memory, 
                    combine_docs_chain_kwargs={'prompt': prompt},
                    verbose=False)