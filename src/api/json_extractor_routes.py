# src/api/json_extractor_routes.py

import json
from fastapi import APIRouter, HTTPException
from src.core.schemas import ExtractionRequest, ExtractionResponse
from src.services import prompt_service, ai_service

router = APIRouter()

@router.post("/extract-json", response_model=ExtractionResponse, summary="Extract JSON from Text")
def handle_json_extraction(request: ExtractionRequest):
    """
    Accepts a block of text and uses a one-shot prompt to extract structured
    information from it, returning the result as a JSON object.
    """
    try:
        # 1. Build the prompt using the prompt service
        final_prompt = prompt_service.create_one_shot_json_prompt(request.text)

        # 2. Get the JSON response from the AI service
        json_string_response = ai_service.get_llm_json_response(final_prompt)

        # 3. Parse the JSON string
        json_data = json.loads(json_string_response)
        
        if "error" in json_data:
             raise HTTPException(status_code=502, detail=json_data["error"])

        return ExtractionResponse(data=json_data)

    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="The AI service returned a non-JSON response.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")