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
Human: {input}
AI:"""


template_retrieval= """<s>[INST] You are nice, honest ai, Given the reference context {context} </s> [/INST]

[INST]answer the following question {question}[/INST]

"""
def create_simple_chat_prompt(template: str = template_chat):
    prompt = ChatPromptTemplate.from_messages(
        [("system",template),
        MessagesPlaceholder(variable_name="history"),
        ("human","{input}")]
    )
    return prompt

def create_simple_prompt(template: str = template):
    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=template
    )
    return prompt


def create_retrieval_prompt(template: str = template_retrieval):
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=template
    )
    return prompt