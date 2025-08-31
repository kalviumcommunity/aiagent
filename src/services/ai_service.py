# src/services/ai_service.py

import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file in the project root
load_dotenv()

# Initialize the OpenAI client. It will automatically find the API key.
client = OpenAI()

def get_llm_json_response(prompt: str) -> str:
    """
    Sends a prompt to the OpenAI API and requests a JSON response.

    Args:
        prompt: The complete prompt to send to the model.

    Returns:
        The content of the model's response as a JSON string.
    """
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY not found. Please set it in your .env file.")

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            # This feature is key for reliable, structured output
            response_format={"type": "json_object"}
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"An error occurred while calling the OpenAI API: {e}")
        return json.dumps({"error": "Failed to get a valid response from the AI service."})