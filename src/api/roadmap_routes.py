# src/api/roadmap_routes.py
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
# Import the new function from ai_service
from ..services import ai_service

router = APIRouter()

# --- Existing Pydantic Model and Endpoint ---
class RoadmapRequest(BaseModel):
    skill: str = Field(..., min_length=2, max_length=100, description="The skill to generate a roadmap for.")

@router.post("/generate-roadmap", status_code=status.HTTP_200_OK)
async def create_roadmap(request: RoadmapRequest):
    try:
        roadmap = await ai_service.generate_roadmap(request.skill)
        return roadmap
    except Exception as e:
        print(f"Error in roadmap generation route: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate roadmap."
        )

# ==============================================================================
#  NEW PYDANTIC MODEL AND ENDPOINT FOR THE CONCEPT EXPLAINER
# ==============================================================================
class ConceptRequest(BaseModel):
    concept: str = Field(..., min_length=2, max_length=100, description="The concept to be explained.")

@router.post("/explain-concept", status_code=status.HTTP_200_OK)
async def get_concept_explanation(request: ConceptRequest):
    """
    Receives a concept and returns a simple, structured explanation.
    """
    try:
        explanation = await ai_service.explain_concept(request.concept)
        return explanation
    except Exception as e:
        print(f"Error in concept explanation route: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate explanation."
        )