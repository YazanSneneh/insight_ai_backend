from pydantic import BaseModel, Field
from typing import TypedDict


class Finding(TypedDict):
    claim: str = Field(..., description="important conclusions")
    explanation: str = Field(..., description="individual important conclusions discovered during research")


class Source(TypedDict):
    title: str = Field(..., description="the title of the link")
    url: str = Field(..., description="the url of the web page")


class ResearchOutPut(TypedDict):
    result: str = Field(..., description="The research done by AI model!")
    title: str = Field(..., description="the title of the research")
    summary: str = Field(..., description="the summary section of the research")
    findings: list[Finding] = Field(..., description="the resources links where the research is built from")
    sources: list[Source] = Field(..., description="the resources links where the research is built from")


class ResearchRequest(BaseModel):
    query: str = Field(..., min_length=1, description="The topic the user wants to research!")


class ResearchResponse(BaseModel):
    title: str = Field(..., description="the title of the research")
    summary: str = Field(..., description="the summary section of the research")
    findings: list[Finding] = Field(..., description="the resources links where the research is built from")
    sources: list[Source] = Field(..., description="the resources links where the research is built from")