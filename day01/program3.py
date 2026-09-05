#import the requited packages
from langchain_ollama import ChatOllama

# create the llm connection
llm = ChatOllama(model="llama3.2:3b")


while True:
    # get input from user
    query = input("> ")

    # check if the user wants to exit
    if query in ["exit", "quit", "q", "stop", "bye","end"]:
        break;

    # send the query to the model
    response = llm.invoke(query)
        
    # print the response
    print(response.content)




