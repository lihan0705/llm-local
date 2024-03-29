from langchain.chains import LLMChain, ConversationChain

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