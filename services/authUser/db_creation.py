from app import db
from app import create_service

auth_service = create_service()

with auth_service.app_context():
    # Drop all existing tables
    db.drop_all()
    print("Dropped all existing tables")
    
    # Create all tables
    db.create_all()
    print("Created all tables successfully")
