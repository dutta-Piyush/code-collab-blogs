from app.model import db
from app import create_service2

content_service = create_service2()


with content_service.app_context():
    db.create_all()
