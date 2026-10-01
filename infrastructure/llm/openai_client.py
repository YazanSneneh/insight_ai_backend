from dotenv import load_dotenv

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()
TOOLS = 
class OpenAIClient():
    def __init__(self, model_name: str ="gpt-5.6-sol", temperature= 0.5, ):
        self.model = ChatOpenAI(model=model_name, temperature=temperature, model_kwargs= { "tools": [{"type": "web_search"}]})
        self.state = {}

    async def ainvoke(self, messages: list[BaseMessage]):
        self.state["messages"] = messages
        self.state["result"] = await self.model.ainvoke(self.state["messages"])

    def get_ai_response(self):
        return self.state["result"]

    def build_system_message(self, query: str) -> SystemMessage:
        return SystemMessage(content=query)

    def build_human_message(self, query: str) -> HumanMessage:
            return HumanMessage(content=query)
