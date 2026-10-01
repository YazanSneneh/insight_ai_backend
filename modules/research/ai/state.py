from typing import TypedDict
from langchain_core.messages import BaseMessage

class ResearchState(TypedDict):
    messages: list[BaseMessage]
    research_result: str