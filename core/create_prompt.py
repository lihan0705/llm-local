from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

template_chat = """
            your answer is always clear and simple but complete "                  
            """

template = """
your answer is always clear and simple but complete
Current conversation:
{history}
Human: {question}
AI:"""


template_retrieval= """
you are nice, honest AI, your answer is always clear and simple but complete
Please answer the question based on the chat history(delimited by <hs></hs>) and context(delimited by <ctx> </ctx>) below.
-----------
<ctx>
{context}
</ctx>
-----------
<hs>
{chat_history}
</hs>
-----------
Question: {question}
Answer:

"""
def create_simple_chat_prompt(template: str = template_chat):
    prompt = ChatPromptTemplate.from_messages(
        [("system",template),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human","{question}")]
    )
    return prompt

def create_simple_prompt(template: str = template):
    prompt = PromptTemplate(
        input_variables=["chat_history", "question"],
        template=template
    )
    return prompt


def create_retrieval_prompt(template_retrieval):
    prompt = PromptTemplate(
        input_variables=["context", "question", "chat_history"],
        template=template_retrieval
    )
    return prompt