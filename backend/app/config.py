import os

class Config:
    SECRET_KEY = "your_secret_key"  # Change this to a random secret key
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"  # Change to your database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
