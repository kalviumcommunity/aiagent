from openai import OpenAI
from config import OPENAI_API_KEY

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=OPENAI_API_KEY)

def get_llm_response(prompt: str) -> str:
    """
    Sends a prompt to the OpenAI API and returns the model's response.

    Args:
        prompt: The complete prompt to send to the model.

    Returns:
        The content of the model's response as a string.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Or any other suitable model like "gpt-3.5-turbo"
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.0, # Temperature 0 for highly deterministic classification
            max_tokens=10    # Small max_tokens as we only expect one word back
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"An error occurred while calling the OpenAI API: {e}")
        return "Error"