from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# model = "gemini-2.5-pro" # or "gemini-2.5-flash"
chat = client.chats.create(
    model="gemini-2.5-pro",
)

def make_questions(topic: str, n: int = 5, level: str = "basic"):
    """
    Ask Gemini to create `n` questions for a given topic and difficulty level.
    Returns the model’s raw text response. You can parse it further if needed.
    """
    prompt = (
        f"Generate {n} {level}-level multiple-choice questions on the topic "
        f"'{topic}'. Provide four options (A–D) for each question and mark "
        "the correct answer with '**'."
    )
    response = chat.send_message(prompt)
    return response.text

# Example: create five basic ML questions
if __name__ == "__main__":
    questions = make_questions(topic="Machine Learning", n=5, level="basic")
    print(questions)
