
from infrastructure.llm.openai_client import OpenAIClient

from .schemas import ResearchOutput
from .prompts import RESEARCH_SYSTEM_PROMPT


class ResearchService():
    def __init__(self):
        self.research_client = OpenAIClient(model_name="gpt-5.6-sol", temperature=0)

    async def research(self, query: str) -> ResearchOutput:
        system_message = self.research_client.build_system_message(query=RESEARCH_SYSTEM_PROMPT)
        human_message = self.research_client.build_human_message(query=query)

        structured_output: OpenAIClient = self.research_client.get_model().with_structured_output(ResearchOutput)
        result: ResearchOutput = await structured_output.ainvoke([system_message, human_message])

        return result
