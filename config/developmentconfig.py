import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('JWT_SECRET')
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

config = {
    'development': DevelopmentConfig,
}