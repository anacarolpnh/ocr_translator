from fastapi import APIRouter
from Controllers.controller_translation import router as translation_router

router = APIRouter()
router.include_router(translation_router, prefix="/api", tags=["translations"])
