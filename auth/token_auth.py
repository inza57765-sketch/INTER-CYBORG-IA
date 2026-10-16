import os
from dotenv import load_dotenv

load_dotenv()
API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROK_API = os.getenv("GROK_API")

def token_verif():
    if GROK_API is not None:
        return GROK_API
    else:
        return None



        