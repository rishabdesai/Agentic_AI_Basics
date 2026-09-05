# Day 02 — Tool Calling
[← Course home](../README.md)

- Tool calling (function calling) is a capability in LLM that allows the model to call external functions or APIs to perform specific tasks.

- A tool is a bridge between the LLM's knowledge and its ability to act, that trasforms the model from passive information source into an active problem solver.

#components of tools: Tool definition, Tool schema & binding, Tool call, Tool execution, Result integration.

## Programs

### Program 1 — 
**File:** [program1.py](program1.py)
- from langchain.tools import tool
  
### Program 2 — 
**File:** [program2.py](program2.py)
- langchain_core.tools import BaseTool
- 
### Program 3 — 
**File:** [program3.py](program3.py)
- from langchain.chat_models import init_chat_model

### Program 4 — 
**File:** [program4.py](program4.py)
- from from langchain_core.prompts import ChatPromptTemplate