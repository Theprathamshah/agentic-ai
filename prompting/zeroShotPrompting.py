import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Zero shot prompting is directly giving the model a task without any examples. The system prompt is used to set the behavior of the model and guide it to generate the desired output. In this example, we are asking the model to review a resume and provide an ATS score along with improvement suggestions. The system instruction is crucial in zero shot prompting as it helps the model understand the context and the expected output format.

SYSTEM_PROMPT = "You are a strict ATS resume evaluator. Only review resumes and return an ATS score out of 100 with improvement suggestions. You should not answer anything except that"

userPrompts = [
    "Review this resume:\nJohn Doe, Software Engineer with 3 years experience in React and Node.js...",
    "Review this resume:\nJane Smith, Data Scientist with 5 years experience in Python and Machine Learning...",
    "Tell me the joke",
    "Who is the president of the United States?",
    "What is the garbage collection in java?"
]

for prompt in userPrompts:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "system_instruction": SYSTEM_PROMPT
        }
    )

    print(response.text)
    print("\n\n")