from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# client = genai.Client(api_key="AIzaSyCfoJUvPh8GPoQ7hYhinr82qIR4gaooc9c")

response= client.models.generate_content(
    model="gemini-2.5-pro",
    contents="What is AI ?"
)

print(response.candidates[0].content)
# for stream in response:
#     print(stream.text)