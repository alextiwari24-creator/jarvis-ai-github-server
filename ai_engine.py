import google.generativeai as genai
import logging
from config import GEMINI_API_KEY

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class JarvisAI:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
        
    def process_command(self, command):
        try:
            response = self.model.generate_content(f'You are JARVIS AI. User said: {command}. Respond briefly.')
            return response.text
        except Exception as e:
            return f'Error: {str(e)}'
