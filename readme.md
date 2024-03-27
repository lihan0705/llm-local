Parent Document Retriever 将chunk切分后，依然可以保证chunk上下文的连续性
chroma vector database
run ollama + langChain (llama2)

# Ollama install
## reference : https://github.com/ollama/ollama
```
curl -fsSL https://ollama.com/install.sh | sh
ollama run llama2
```
# langchain 
1. Conversational Memory, Definition: Memory is an agent's capacity of remembering previous interactions with the user (think chatbots)




error case: 1. Import error : cannot import name 'open_filename' from 'pdfminer.utils', please pip uninstall pdfminer, pip install pdfminer.six



