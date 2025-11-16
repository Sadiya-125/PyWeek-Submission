import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL

def get_gemini_response(prompt: str) -> str:
    """Get text response from Gemini AI"""
    if not GEMINI_API_KEY:
        return "Error: GEMINI_API_KEY not found. Please set it in your .env file"
    
    try:
        # Configure Gemini API with the key
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error from Gemini: {str(e)}"
