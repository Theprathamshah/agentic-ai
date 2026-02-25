import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Review this resume:\nJohn Doe, Software Engineer with 3 years experience in React and Node.js...",
    config={
        "system_instruction": "You are a strict ATS resume evaluator. Only review resumes and return an ATS score out of 100 with improvement suggestions. You should not answer anything except that"
    }
)

print(response.text)