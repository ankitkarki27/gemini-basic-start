from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
from pathlib import Path

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# for uploaded file
# uploaded_file = client.files.upload(file="amazon-icon.png")

img_path = Path(__file__).parent / "assets" / "cv.pdf" 
if not img_path.exists():
    raise FileNotFoundError(img_path)

uploaded_file = client.files.upload(file=str(img_path))


#for response
response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents=["Describe this pdf for me", uploaded_file]
)

print(response.text)
