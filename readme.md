Parent Document Retriever 将chunk切分后，依然可以保证chunk上下文的连续性
chroma vector database
run ollama + langChain (llama2)

# Ollama install
## reference : https://github.com/ollama/ollama
```
curl -fsSL https://ollama.com/install.sh | sh
ollama run llama2:13b , ollama run mixtral:8x7b
ollama pull nomic-embed-text # pull embeddings model
```
# langchain learning note
0. chain = prompt | llm | parser | memory  / LLMChain(llm,prompt,memory)
1. Conversational Memory, Definition: Memory is an agent's capacity of remembering previous interactions with the user (think chatbots)
2. ChatPromptTemplate.from_messages([('system','be honest. \nFormatting Instructions: {format_instructions}]'), 
                                     ('human','{input}')])
3. StrOutputParser() convert message to different output format  
   JsonOutputParser(pydantic_object=Person) Person(Basemodel)          
4. Document(page_content="")  / create_stuff_documents_chain   / WeebBaseLoader  /  RecursiveCharacterTextSplitter
5. OpenAIEmbeddings -> faiss(vectorstores) -> .as_retriever -> create_retrieval_chain
6. Agent, OpenAI function Agent, AgentExecutor a. TavilySearchResults b. create_retriever_tool
7. autogen




error case: 1. Import error : cannot import name 'open_filename' from 'pdfminer.utils', please pip uninstall pdfminer, pip install pdfminer.six



