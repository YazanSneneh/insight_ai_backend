

from infrastructure.llm.openai_client import OpenAIClient
from .prompts import RESEARCH_SYSTEM_PROMPT

class ResearchService():
    def __init__(self):
        self.research_client = OpenAIClient(model_name="gpt-5.6-sol", temperature=0)

    async def research(self, query: str):
        system_message = self.research_client.build_system_message(query=RESEARCH_SYSTEM_PROMPT)
        human_message = self.research_client.build_human_message(query=query)

        await self.research_client.ainvoke([system_message, human_message])

        return self.format_research_response()

    def format_research_response(self):
        content = self.research_client.get_ai_response().content
        return "\n".join( block["text"] for block in content if block.get("type") == "text")
