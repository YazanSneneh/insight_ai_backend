from pydantic import BaseModel, Field


class Source(BaseModel):
    title: str = Field(..., description="the title of the link")
    url: str = Field(..., description="the url of the web page")

class Finding(BaseModel):
    claim: str = Field(..., description="important conclusions")
    explanation: str = Field(..., description="individual important conclusions only discovered during research")
    source: Source = Field(..., description="the url that back the claim")


class ResearchOutput(BaseModel):
    title: str = Field(..., description="the title of the research")
    summary: str = Field(..., description="the summary section of the research")
    findings: list[Finding] = Field(..., description="the resources links where the research is built from", max_length=3)
    sources: list[Source] = Field(..., description="the resources links where the research is built from", min_length=2, max_length=4)


class ResearchRequest(BaseModel):
    query: str = Field(..., min_length=1, description="The topic the user wants to research!")


class ResearchResponse(BaseModel):
    title: str = Field(..., description="the title of the research")
    summary: str = Field(..., description="the summary section of the research")
    findings: list[Finding] = Field(..., description="the resources links where the research is built from", max_length=3)
    sources: list[Source] = Field(..., description="the resources links where the research is built from", min_length=2, max_length=4)