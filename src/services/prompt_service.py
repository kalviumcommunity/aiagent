# src/services/prompt_service.py

# (Keep any other functions you already have in this file)

def create_one_shot_json_prompt(user_query: str) -> str:
    """
    Loads the one-shot JSON extractor prompt from the root prompts/ directory
    and formats it with the user's query.

    Args:
        user_query: The text from which to extract information.

    Returns:
        The fully formatted prompt ready to be sent to the LLM.
    """
    try:
        # This path is relative to the project root (AIAGENT), where you run uvicorn.
        with open('prompts/one_shot_json_extractor.txt', 'r') as f:
            prompt_template = f.read()
    except FileNotFoundError:
        raise FileNotFoundError("Prompt template 'prompts/one_shot_json_extractor.txt' not found.")

    # Inject the user query into the template
    return prompt_template.format(user_query=user_query)