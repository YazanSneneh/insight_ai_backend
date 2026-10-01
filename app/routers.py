from fastapi import APIRouter

from modules.research.router import research_router

routers: APIRouter = APIRouter(prefix="/v1")

routers.include_router(research_router)
