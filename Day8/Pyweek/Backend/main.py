# python main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from gemini_service import get_gemini_response
from sarvam_service import text_to_speech
from config import BACKEND_HOST, BACKEND_PORT

app = FastAPI(title="AI Bot Backend")

# CORS middleware for Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    text_input: str

class QueryResponse(BaseModel):
    text_output: str
    text_audio: str  # Base64 encoded audio

@app.post("/askAI", response_model=QueryResponse)
async def ask_ai(query: QueryRequest):
    """Main endpoint combining Gemini and Sarvam AI"""
    try:
        # Get response from Gemini
        gemini_response = get_gemini_response(query.text_input)
        
        # Convert to audio using Sarvam
        audio_base64 = text_to_speech(gemini_response)
        
        return QueryResponse(
            text_output=gemini_response,
            text_audio=audio_base64
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "AI Bot Backend is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=BACKEND_HOST, port=BACKEND_PORT)
