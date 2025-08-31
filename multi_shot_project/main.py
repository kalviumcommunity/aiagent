import llm_interface

def run_multi_shot_example():
    """
    Demonstrates multi-shot prompting by classifying text sentiment.
    """
    # 1. Define the new user query to be classified
    user_query = "I'm not sure how I feel about the new color scheme, but the login process is definitely easier."

    # 2. Load the multi-shot prompt template from the external file
    try:
        with open('prompts/multi_shot_sentiment.txt', 'r') as f:
            prompt_template = f.read()
    except FileNotFoundError:
        print("Error: prompts/multi_shot_sentiment.txt not found.")
        return

    # 3. Inject the user query into the prompt template.
    #    The multi-shot examples are already part of the template.
    final_prompt = prompt_template.format(user_query=user_query)

    print("--- FINAL PROMPT SENT TO LLM ---")
    print(final_prompt)
    print("--------------------------------\n")

    # 4. Get the classification from the LLM
    sentiment = llm_interface.get_llm_response(final_prompt)

    print(f"--- LLM RESPONSE ---")
    print(f"Text to Analyze: '{user_query}'")
    print(f"Predicted Sentiment: {sentiment}")
    print("--------------------")


if __name__ == "__main__":
    run_multi_shot_example()