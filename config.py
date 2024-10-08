# config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///school.db'  # SQLite for simplicity
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # For session management, etc.
