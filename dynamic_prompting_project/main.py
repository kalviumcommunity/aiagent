import llm_interface

def run_chain_of_thought_example():
    """
    Demonstrates Chain-of-Thought prompting by solving a math word problem.
    """
    # 1. Define the new, multi-step problem for the AI to solve
    user_question = "A library has 5 bookshelves. Each bookshelf has 4 shelves. If a librarian places 10 books on each shelf, how many books are in the library in total?"

    # 2. Load the Chain-of-Thought prompt template
    try:
        with open('prompts/cot_math_problem.txt', 'r') as f:
            prompt_template = f.read()
    except FileNotFoundError:
        print("Error: prompts/cot_math_problem.txt not found.")
        return

    # 3. Inject the user's question into the prompt
    final_prompt = prompt_template.format(user_question=user_question)

    print("--- FINAL PROMPT SENT TO LLM ---")
    print(final_prompt)
    print("--------------------------------\n")

    # 4. Get the full response from the LLM (including its reasoning)
    ai_response = llm_interface.get_llm_response(final_prompt)

    print("--- LLM's Full Response (including Chain of Thought) ---")
    # We prepend "Thought:" because the model's output will start after that cue
    print("Thought:")
    print(ai_response)
    print("--------------------------------------------------------")

    # Optional: You can parse the final answer from the response
    try:
        final_answer = ai_response.split("Answer:")[1].strip()
        print(f"\nExtracted Final Answer: {final_answer}")
    except IndexError:
        print("\nCould not extract a final answer from the response.")


if __name__ == "__main__":
    run_chain_of_thought_example()