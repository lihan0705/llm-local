# Controllable Agents for RAG

# pip install llama-index-agent-openai
# pip install llama-index-llms-openai
# pip install llama-index
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from core.create_llm_model import create_ollama_model
from core.load_documents import load_pdf_llamaIndex
from core.create_agent import get_tool

from llama_index.core.agent import AgentRunner, ReActAgent
from llama_index.agent.openai import OpenAIAgentWorker, OpenAIAgent
from llama_index.agent.openai import OpenAIAgentWorker


def chat_repl(agent, exit_when_done: bool = True):
    """Chat REPL.

    Args:
        exit_when_done(bool): if True, automatically exit when step is finished.
            Set to False if you want to keep going even if step is marked as finished by the agent.
            If False, you need to explicitly call "exit" to finalize a task execution.

    """
    task_message = None
    while task_message != "exit":
        task_message = input(">> Human: ")
        if task_message == "exit":
            break

        task = agent.create_task(task_message)

        response = None
        step_output = None
        message = None
        while message != "exit":
            if message is None or message == "":
                step_output = agent.run_step(task.task_id)
            else:
                step_output = agent.run_step(task.task_id, input=message)
            if exit_when_done and step_output.is_last:
                print(
                    ">> Task marked as finished by the agent, executing task execution."
                )
                break

            message = input(
                ">> Add feedback during step? (press enter/leave blank to continue, and type 'exit' to stop): "
            )
            if message == "exit":
                break

        if step_output is None:
            print(">> You haven't run the agent. Task is discarded.")
        elif not step_output.is_last:
            print(">> The agent hasn't finished yet. Task is discarded.")
        else:
            response = agent.finalize_response(task.task_id)
        print(f"Agent: {str(response)}")



def main():
    file_path_lidar4d = ["lidar4d.pdf"]
    file_path_bevfusion = ["bevfusion.pdf"]
    doc_lidar4d = load_pdf_llamaIndex(file_path_lidar4d)
    doc_bevfusion = load_pdf_llamaIndex(file_path_bevfusion)
    Paper_lidar4d_tool = get_tool("lidar4d", "Lidar4d", documents=doc_lidar4d)
    Paper_bevfusion = get_tool("lidar4d", "Lidar4d", documents=doc_bevfusion)

    llm = create_ollama_model()
    query_engine_tools = [Paper_lidar4d_tool, Paper_bevfusion]

    agent = ReActAgent.from_tools(
        query_engine_tools, llm=llm, verbose=True, max_iterations=20
    )

    chat_repl(agent)

if __name__ == "__main__":
    main()
