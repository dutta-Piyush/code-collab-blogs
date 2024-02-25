from app.model import User
from app import create_service

auth_service = create_service()

with auth_service.app_context():
    all_data = User.query.all()

print(all_data)

for row in all_data:
    print(f"\n\n\nID: {row.id},"
          f"\nFirst_Name: {row.first_name},"
          f"\nLast_Name: {row.last_name},"
          f"\nEmail: {row.email},"
          f"\npassword: {row.password}")
