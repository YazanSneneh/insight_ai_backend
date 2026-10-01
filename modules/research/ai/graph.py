from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langgraph.graph import StateGraph, START, END

from .state import ResearchState
from .nodes import research_node
from .prompts import RESEARCH_SYSTEM_PROMPT


research_graph = StateGraph(ResearchState)

research_graph.add_node("research_node", research_node)

research_graph.add_edge(START, "research_node")
research_graph.add_edge("research_node", END)

research_agent = research_graph.compile()

async def get_research_result(query: str) -> str:
    system_message = SystemMessage(content=RESEARCH_SYSTEM_PROMPT)
    human_message: HumanMessage = HumanMessage(content=query)

    response = await research_agent.ainvoke({"messages": [system_message, human_message]})

    return response["research_result"]