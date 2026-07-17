import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
DB_PATH = os.getenv("DB_PATH", "data/app.db")
