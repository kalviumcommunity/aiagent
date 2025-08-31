from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def get_llm_response(prompt: str) -> str:
    """Sends a prompt to the OpenAI API and returns the model's response."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.1, # Low temperature for logical, deterministic reasoning
            max_tokens=300   # Allow enough space for the thought process and answer
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"An error occurred while calling the OpenAI API: {e}")
        return "Error: Could not get a response from the AI."