# config.py

class Config:
    SECRET_KEY = "This is a secret key!"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///User.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
