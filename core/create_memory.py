from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory

def create_conversation_buffer_memory():
    buffer_memory = ConversationBufferMemory(
                        memory_key="chat_history",
                        input_key="input")
    return buffer_memory


def create_conversation_summary_memory(llm):
    buffer_memory = ConversationSummaryMemory(llm=llm, memory_key="chat_history")
    return buffer_memory