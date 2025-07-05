from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# for uploaded file
uploaded_file = client.files.upload(file="assets/amazon-icon.png")

#for response
response = client.files.generate_content(
    model="gemini-2.5-pro",
    contents=["Describe this image for me", uploaded_file]
)

print(response.text)
