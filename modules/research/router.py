from typing import Annotated
from fastapi import APIRouter, Query, status

from .schemas import ResearchRequest, ResearchResponse
from .service import ResearchService

research_router: APIRouter = APIRouter(prefix="/research")

@research_router.get("/")
async def research(research_params: Annotated[ResearchRequest, Query()]) -> ResearchResponse:
    research_service = ResearchService()
    research_result = await research_service.research(research_params.query)
    return ResearchResponse(result=research_result, status_code=status.HTTP_200_OK)