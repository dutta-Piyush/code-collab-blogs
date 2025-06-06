# config.py
import os


class Config:
    SECRET_KEY = "b5c264c248a78049777ca91db165ad40076e1249e1351512da1f92b3afba60fa"
    # Force using localhost for local development
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/mydatabase"
    # basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "instance", "code_collab_blogs.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Session Configuration
    SESSION_COOKIE_SECURE = False  # Set to True in production with HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'  # Better security than 'None'


