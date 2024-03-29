from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory

def create_conversation_buffer_memory():
    buffer_memory = ConversationBufferMemory(
                        memory_key="history",
                        return_messages=True)
    return buffer_memory