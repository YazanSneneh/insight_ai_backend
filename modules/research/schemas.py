from pydantic import BaseModel, Field

class ResearchRequest(BaseModel):
    query: str = Field(..., description="The topic the user wants to research!")


class ResearchResponse(BaseModel):
    result: str = Field(..., description="The research done by AI model!")