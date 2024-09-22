import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    JWT_EXPIRATION_DELTA = 3600  # JWT expiration time in seconds
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/1')
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///database.db')
