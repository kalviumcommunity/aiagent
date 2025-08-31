# src/core/schemas.py

from pydantic import BaseModel
from typing import Dict, Any

class ExtractionRequest(BaseModel):
    """Defines the structure for the incoming API request."""
    text: str

class ExtractionResponse(BaseModel):
    """Defines the structure for the outgoing API response."""
    data: Dict[str, Any]