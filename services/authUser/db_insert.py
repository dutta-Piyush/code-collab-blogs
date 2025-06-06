from app import create_service
from app.model import User, Content, db
from werkzeug.security import generate_password_hash
import uuid

auth_service = create_service()

def insert_dummy_data():
    with auth_service.app_context():
        # Create dummy users
        user1 = User(
            id=str(uuid.uuid4()),
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            password=generate_password_hash("password123")
        )

        user2 = User(
            id=str(uuid.uuid4()),
            first_name="Jane",
            last_name="Smith",
            email="jane@example.com",
            password=generate_password_hash("password456")
        )

        # Add users to database
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        print("Users created successfully!")

        # Create dummy content
        content1 = Content(
            title="First Blog Post",
            content="This is my first blog post. Welcome to my blog!",
            id=user1.id
        )

        content2 = Content(
            title="Second Blog Post",
            content="This is another interesting post about technology.",
            id=user1.id
        )

        content3 = Content(
            title="Jane's First Post",
            content="Hello everyone! This is Jane's first post.",
            id=user2.id
        )

        # Add content to database
        db.session.add(content1)
        db.session.add(content2)
        db.session.add(content3)
        db.session.commit()

        print("Content created successfully!")

if __name__ == "__main__":
    insert_dummy_data() 