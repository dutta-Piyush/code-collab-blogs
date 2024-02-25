from app import db
from app import create_service

server = create_service()


with server.app_context():
    db.create_all()
