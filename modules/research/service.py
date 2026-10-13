
from infrastructure.llm.openai_client import OpenAIClient

from .schemas import ResearchOutPut
from .prompts import RESEARCH_SYSTEM_PROMPT


class ResearchService():
    def __init__(self):
        self.research_client = OpenAIClient(model_name="gpt-5.6-sol", temperature=0)

    async def research(self, query: str) -> ResearchOutPut:
        system_message = self.research_client.build_system_message(query=RESEARCH_SYSTEM_PROMPT)
        human_message = self.research_client.build_human_message(query=query)

        structured_poutput = self.research_client.get_model().with_structured_output(ResearchOutPut)
        result: ResearchOutPut = await structured_poutput.ainvoke([system_message, human_message])

        return result
