# Ollama 🦙 Installation Guide

Welcome to Ollama! 🎉 This repository provides tools for conversational AI development, including various utilities and models. Below are the instructions to install and set up the Ollama environment.

## Installation Process 🛠️

To install Ollama, follow these steps:

1. Run the following command in your terminal:

    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```

2. After installation, you can run specific models using commands like:

    ```bash
    ollama run llama2:13b
    ollama run mixtral:8x7b
    ```

3. Additionally, you can pull specific resources like embeddings models using the following command:

    ```bash
    ollama pull nomic-embed-text
    ```

## Langchain Learning Note 📚

### Overview 🔍

The Langchain learning note provides insights into the architecture and components of conversational agents developed using Ollama tools. Here are some key points:

1. **Chain Architecture**: The conversational agent consists of several components arranged in a chain, including the Language Model (LLM), parser, and memory. This architecture enables various functionalities like conversation handling and retrieval.

2. **Conversational Memory**: Memory is crucial for agents to remember previous interactions with users. It helps in maintaining context and providing more coherent responses.

3. **ChatPromptTemplate**: This utility allows for flexible formatting of chat prompts, facilitating clear communication between the system and users.

4. **Output Parsing**: Various output formats can be parsed using utilities like `StrOutputParser` and `JsonOutputParser`, enhancing the versatility of the conversational agent.

5. **Document Processing**: Utilities like `Document` and `WeebBaseLoader` aid in handling document-based interactions, such as extracting text from PDF files.

6. **Retrieval Mechanism**: The system incorporates a retrieval mechanism using OpenAI embeddings and Faiss for efficient document retrieval and response generation.

7. **Agent Execution**: The Ollama framework provides functions for executing agents and handling search results, streamlining the development process.

### Troubleshooting ⚠️

In case of import errors related to `pdfminer`, consider uninstalling and reinstalling `pdfminer.six` using the following commands:

```bash
pip uninstall pdfminer
pip install pdfminer.six