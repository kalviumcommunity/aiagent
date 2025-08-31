from pathlib import Path

def create_dynamic_explanation_prompt(concept: str, expertise_level: str) -> str:
    """
    Dynamically builds a prompt by selecting and assembling components
    based on the user's expertise level.

    Args:
        concept: The technical concept to be explained.
        expertise_level: The user's expertise ('Beginner', 'Intermediate', 'Advanced').

    Returns:
        The fully assembled prompt string.
    """
    # Define the base path for our prompt components
    prompt_dir = Path('prompts/dynamic_explainer')

    # 1. Load the base prompt template
    try:
        base_prompt = (prompt_dir / 'base_prompt.txt').read_text()
    except FileNotFoundError:
        raise FileNotFoundError("Could not find the base prompt template.")

    # 2. Select the expertise instructions dynamically
    expertise_map = {
        "Beginner": "expertise_beginner.txt",
        "Intermediate": "expertise_intermediate.txt",
        "Advanced": "expertise_advanced.txt",
    }

    expertise_filename = expertise_map.get(expertise_level)
    if not expertise_filename:
        raise ValueError(f"Invalid expertise level: {expertise_level}")

    try:
        expertise_instructions = (prompt_dir / expertise_filename).read_text()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find the prompt file for {expertise_level} expertise.")

    # 3. Assemble the final prompt by filling in the placeholders
    final_prompt = base_prompt.format(
        concept=concept,
        expertise_level=expertise_level,
        expertise_instructions=expertise_instructions
    )

    return final_prompt