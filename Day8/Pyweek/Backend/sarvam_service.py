import requests
from config import SARVAM_API_KEY

SARVAM_TTS_URL = "https://api.sarvam.ai/text-to-speech"

def text_to_speech(text: str) -> str:
    """Convert text to speech using Sarvam AI and return base64 audio"""
    try:
        headers = {
            "api-subscription-key": SARVAM_API_KEY,
            "Content-Type": "application/json"
        }
        
        payload = {
            "text": text,  # Single text string (max 1500 chars)
            "target_language_code": "hi-IN",  # English-India
            "speaker": "anushka",  # Female voice (valid for v2)
            "pitch": 0.8,
            "pace": 1.0,
            "loudness": 2.5,
            "speech_sample_rate": 22050,  # Default sample rate
            "enable_preprocessing": True,
            "model": "bulbul:v2"  # Latest model
        }
        
        response = requests.post(SARVAM_TTS_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            audio_data = response.json().get("audios", [None])[0]
            return audio_data if audio_data else ""
        else:
            print(f"Sarvam API Error: {response.status_code} - {response.text}")
            return ""
    except Exception as e:
        print(f"Sarvam TTS Error: {str(e)}")
        return ""
