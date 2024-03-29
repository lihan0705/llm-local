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