from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Supertelligence Backend", version="1.0.0")

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    message: str
    user_id: str
    username: str

class ChatResponse(BaseModel):
    response: str
    user_id: str

@app.get("/")
async def root():
    return {"message": "Supertelligence Backend is running!"}

@app.post("/chat", response_model=ChatResponse)
async def chat_with_llm(request: ChatRequest):
    try:
        # Create a chat completion with OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Supertelligence, a helpful AI assistant integrated with Discord. You're knowledgeable, friendly, and concise in your responses."},
                {"role": "user", "content": request.message}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        
        return ChatResponse(
            response=ai_response,
            user_id=request.user_id
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 