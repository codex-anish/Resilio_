import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
AUTHORITY_API = os.getenv("AUTHORITY_API")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY missing")

if not AUTHORITY_API:
    raise RuntimeError("AUTHORITY_API missing")
