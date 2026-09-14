import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
SERVER_PORT = int(os.getenv('SERVER_PORT', 5000))
SERVER_HOST = os.getenv('SERVER_HOST', '0.0.0.0')
VOICE_ENABLED = os.getenv('VOICE_ENABLED', 'true').lower() == 'true'
WAKE_WORD = 'jarvis'
