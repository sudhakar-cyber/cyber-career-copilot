import os
from datetime import timedelta
from dotenv import load_dotenv

# Load .env file from project root
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise RuntimeError("Please set SECRET_KEY in your .env file")
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    DEBUG = FLASK_ENV == 'development'
    PORT = int(os.environ.get('PORT', 5000))

    # MySQL Database Settings
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'cyber_career_copilot')
    USE_SQLITE_FALLBACK = os.environ.get('USE_SQLITE_FALLBACK', 'True').lower() in ('true', '1', 't', 'yes')
    SQLITE_DB_PATH = os.path.join(basedir, 'cyber_career_copilot.db')

    # AI API Keys
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '').strip()
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '').strip()

    # Session settings
    SESSION_COOKIE_NAME = 'cyber_copilot_session'
    SESSION_COOKIE_PATH = '/'
    SESSION_COOKIE_SECURE = False  # Allows persistent session cookie on localhost HTTP
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)  # Keep user logged in across refreshes and restarts
