from typing import Annotated
from fastapi import APIRouter, Query, status

from .schemas import ResearchRequest, ResearchResponse
from .ai.graph import get_research_result

research_router: APIRouter = APIRouter(prefix="/research")

@research_router.get("/")
async def research(research_params: Annotated[ResearchRequest, Query()]) -> ResearchResponse:
    result = await get_research_result(research_params.query)

    return ResearchResponse(result=result, status_code=status.HTTP_200_OK)