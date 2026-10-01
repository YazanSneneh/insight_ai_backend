from dotenv import load_dotenv

from .state import ResearchState
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-5.6-sol", temperature=0.9, model_kwargs={ "tools": [{"type": "web_search"}]})

async def research_node(state: ResearchState) -> ResearchState:
    """ the node is responsible for doing a research for a topic requested by user via AI"""
    
    response =  await model.ainvoke(state.get("messages"))
    research_result = "\n".join( block["text"] for block in response.content if block.get("type") == "text")
    state["research_result"] = research_result
    return state