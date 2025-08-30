# src/services/ai_service.py
import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from . import prompt_service

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ... (the existing generate_roadmap function is here) ...
async def generate_roadmap(skill: str) -> dict:
    # (no changes to this function)
    system_prompt = prompt_service.load_prompt('roadmap_generator', 'system')
    user_prompt_template = prompt_service.load_prompt('roadmap_generator', 'user')
    user_prompt = prompt_service.format_user_prompt(user_prompt_template, {'skill': skill})
    # (mock response or API call logic remains)
    mock_ai_response = { "skill": skill, "roadmap": [] }
    return mock_ai_response


# ==============================================================================
#  NEW FUNCTION TO ADD FOR THE ZERO-SHOT CONCEPT EXPLAINER
# ==============================================================================
async def explain_concept(concept: str) -> dict:
    """
    Generates a simple explanation for a concept using a zero-shot prompt.
    
    Args:
        concept: The concept the user wants to understand.
        
    Returns:
        A dictionary containing the parsed JSON explanation from the AI.
    """
    # 1. Load the specific prompts for this task
    system_prompt = prompt_service.load_prompt('concept_explainer', 'system')
    user_prompt_template = prompt_service.load_prompt('concept_explainer', 'user')

    # 2. Format the user prompt with the specific concept
    user_prompt = prompt_service.format_user_prompt(user_prompt_template, {'concept': concept})

    print('--- Sending to AI for Explanation ---')
    print(f'System: {system_prompt[:100]}...')
    print(f'User: {user_prompt}')
    print('-------------------------------------')

    # 3. Call the AI model (real call is commented out)
    # try:
    #     response = client.chat.completions.create(
    #         model="gpt-4-1106-preview",
    #         messages=[
    #             {"role": "system", "content": system_prompt},
    #             {"role": "user", "content": user_prompt},
    #         ],
    #         response_format={"type": "json_object"},
    #     )
    #     return json.loads(response.choices[0].message.content)
    # except Exception as e:
    #     print(f"An error occurred with the OpenAI API call: {e}")
    #     raise

    # Mocked response for demonstration
    mock_explanation = {
        "concept": concept,
        "analogy": "Think of an API like a waiter in a restaurant. You don't go to the kitchen to get your food; you give your order to the waiter, who communicates with the kitchen and brings the food back to you.",
        "definition": "An API (Application Programming Interface) is a set of rules that allows different software applications to talk to each other.",
        "key_points": [
            "It acts as an intermediary, simplifying complex processes.",
            "APIs allow developers to use existing services without needing to know their internal workings."
        ]
    }
    return mock_explanation