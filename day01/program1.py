##pip install langchain langchain-ollama langchain-openai

#import the required packages
from langchain_ollama import ChatOllama

#create the instance of ChatOllama
llm = ChatOllama(model="llama3.2:3b")

#user prompt
prompt = "What is the capital of India?"

#response from the model
response = llm.invoke(prompt)

#print the response
print(response.content)
