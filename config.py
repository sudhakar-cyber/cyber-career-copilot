import os
from dotenv import load_dotenv

# Load .env file from project root
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'cyber_copilot_default_development_key_2026')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    DEBUG = FLASK_ENV == 'development'
    PORT = int(os.environ.get('PORT', 5000))

    # MySQL Database Settings
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'root')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'cyber_career_copilot')
    USE_SQLITE_FALLBACK = os.environ.get('USE_SQLITE_FALLBACK', 'True').lower() in ('true', '1', 't', 'yes')
    SQLITE_DB_PATH = os.path.join(basedir, 'cyber_career_copilot.db')

    # AI API Keys
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '').strip()
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '').strip()

    # Session settings
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = 86400  # 24 hours
