## About The Project

Elevate7 is a Generative AI-powered mentor designed to help users master any new skill in a structured, 7-day program. It creates a personalized, adaptive roadmap, provides daily plans and resources, evaluates progress through quizzes, and dynamically guides the user step-by-step.

Our goal is to make learning efficient, engaging, and accessible to everyone, powered by cutting-edge AI.

---

## ✨ Features

Elevate7 is packed with powerful features to create a seamless learning experience:

*   **📅 7-Day Roadmap Generator**: Automatically creates a logical, step-by-step learning plan for any skill.
*   **🤖 Dynamic Prompting**: The AI mentor adapts its guidance based on user progress and specific queries.
*   **🔍 Embeddings + Vector Database**: Delivers highly accurate and context-aware answers when users ask questions.
*   **🧩 One-shot & Multi-shot Prompting**: Customizes the learning experience by providing concise or detailed explanations as needed.
*   **🧠 Chain of Thought Reasoning**: Generates coherent and logical plans by breaking down complex skills into manageable steps.
*   **📂 Structured Output (JSON)**: Ensures that all generated content is well-organized and easy to display in a user interface.
*   **🔗 Function Calling**: Fetches relevant external resources like documentation, cheat sheets, or videos to supplement learning.
*   **✅ Daily Quiz/Task**: Evaluates user progress and reinforces learning through mini-assessments.
*   **🛑 Stop Sequences**: Keeps AI responses concise, focused, and highly readable.

---

## ⚙️ How It Works

1.  **Input Skill**: The user specifies the skill they want to learn.
2.  **Generate Roadmap**: The AI uses Chain of Thought reasoning to generate a structured 7-day plan in JSON format.
3.  **Daily Learning**: Each day, the user receives a set of tasks, resources (fetched via Function Calling), and explanations.
4.  **Interact & Adapt**: The user can ask questions (answered via the Vector Database) and the AI dynamically adjusts its prompts based on the user's progress.
5.  **Evaluate**: The user completes a daily quiz or task to test their knowledge.
6.  **Mastery**: After 7 days, the user has a foundational understanding of the skill.

---

## 🛠️ Technology Stack

*   **Frontend**: React, Vite, CSS Modules
*   **Backend**: Node.js, Express.js
*   **AI/LLM**: OpenAI API (GPT-4) / Google Gemini
*   **Vector Database**: Pinecone / Weaviate
*   **Database**: PostgreSQL / MongoDB (for user data)
*   **Deployment**: Docker, Vercel (for frontend), AWS/GCP (for backend)

---
