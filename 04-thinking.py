from google import genai
from google.genai import types          
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


cfg = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
        thinking_budget=1024,         
        include_thoughts=True          
    )
)

response = client.models.generate_content(
    model="gemini-2.5-flash",          # or gemini-2.5-pro
    contents="Generate a 30-day AI/ML learning plan for beginners",
    config=cfg
)

print("AIBot:\n", response.text)

# Show the thought summary that comes back with include_thoughts=True
for part in response.candidates[0].content.parts:
    if part.thought:                   # summary of the model’s own reasoning
        print("\nThought summary:\n", part.text)
