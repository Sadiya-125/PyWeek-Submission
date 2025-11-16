import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

# API Configuration
BACKEND_HOST = "0.0.0.0"
BACKEND_PORT = 8000

# Model Settings
GEMINI_MODEL = "gemini-2.5-pro"
