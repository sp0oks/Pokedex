import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(64))
    MONGODB_URL = os.getenv('MONGODB_URL', 'mongodb://mongo:27017/')

