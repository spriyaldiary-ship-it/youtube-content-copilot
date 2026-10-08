import os

from dotenv import load_dotenv
from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="YouTube Content Copilot API",
    version="0.1.0"
)

client = OpenAI(api_key=api_key)


class ContentRequest(BaseModel):
    topic: str
    language: str
    content_type: str
    audience: str
    tone: str
    duration: str


@app.get("/")
def root():
    return {
        "message": "YouTube Content Copilot API is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/content/create")
def create_content(request: ContentRequest):

    prompt = f"""
You are a natural Tamil YouTube content writer for the MARUPAKKAM channel.

Create engaging, human-sounding YouTube content.

Topic: {request.topic}
Language: {request.language}
Content type: {request.content_type}
Audience: {request.audience}
Tone: {request.tone}
Duration: {request.duration}

IMPORTANT:
- Write naturally for YouTube viewers.
- If the language is Tamil, use simple spoken Tamil.
- Avoid overly formal or literary Tamil.
- Make it sound like a real person talking.
- Use everyday-life examples.
- Keep the storytelling engaging.

Create:

1. Video Title
2. Strong Hook
3. Introduction
4. Main Story / Main Points
5. Real-life Examples
6. Emotional Insight
7. Conclusion
8. Call to Action

Write the complete response in {request.language}.
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return {
        "message": "AI content generated successfully!",
        "topic": request.topic,
        "generated_content": response.output_text
    }
