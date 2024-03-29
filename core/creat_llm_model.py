from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


def create_ollama_model(temperature: float = 1):
    llm = Ollama(model="gemma:7b", temperature=temperature, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
    return llm