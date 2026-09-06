
#simple stateless agent example using langchain

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.messages import HumanMessage


#create model connection
model = init_chat_model(model="llama3.2:3b", model_provider="ollama")

#system prompt
system_prompt = "You are a helpful assistant."
 

#create agent
agent = create_agent(model=model, system_prompt=system_prompt)


while True:
    query = input("> ")
    if query in ['exit', 'quit']:
        break

    #send the query to agent
    # response = agent.invoke({"messages": [
    #     {'role': 'user', 'content': query}
    # ]})
    response = agent.invoke({
        "messages": [HumanMessage(content=query)]
    })

    #print the response
    print(response['messages'][-1].content)