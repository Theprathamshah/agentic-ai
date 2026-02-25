import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are a strict ATS resume evaluator.

Rules:
1. Only evaluate TECH resumes.
2. If resume is non-tech, reply exactly:
   I can't evaluate non tech related resume and jobs.
3. If asked anything unrelated to resume review, reply exactly:
   sorry
4. Always follow the exact output format below.

Output Format:
ATS Score: <number>/100
Improvements:
1. <point>
2. <point>
3. <point>
"""

few_shot_contents = [
    types.Content(
        role="user",
        parts=[types.Part(text="Review this resume:\nBackend Developer with 2 years experience in Java and Spring Boot.")]
    ),
    types.Content(
        role="model",
        parts=[types.Part(text="""ATS Score: 65/100
Improvements:
1. Add measurable achievements.
2. Include keywords like REST APIs, Microservices.
3. Add GitHub links.""")]
    ),
]

user_prompts = [
    "Review this resume:\nJohn Doe, Software Engineer with 3 years experience in React and Node.js...",
    "Review this resume:\nJane Smith, Data Scientist with 5 years experience in Python and Machine Learning...",
    "I am chaterd accountant with 10 years experience in auditing and taxation. Review my resume",
    "Tell me a joke",
]

for prompt in user_prompts:
    contents = few_shot_contents + [
        types.Content(
            role="user",
            parts=[types.Part(text=prompt)]
        )
    ]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0,
        ),
    )

    print("Prompt:", prompt)
    print("Response:")
    print(response.text)
    print("=" * 60)