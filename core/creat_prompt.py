from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

sys_prompt = """
                you are a nice, honest, helpful AI assistant. 
                your answer is always efficient and concise, 
                you are here to assist me.
             """

def creat_simple_prompt(sys_prompt: str = sys_prompt):
    prompt = ChatPromptTemplate.from_messages([
        ("system", sys_prompt),
        ("human", "{input}")
    ])
    return prompt