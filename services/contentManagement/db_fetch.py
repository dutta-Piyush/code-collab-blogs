from app.model import Content
from app import create_service2

content_service = create_service2()

with content_service.app_context():
    all_data = Content.query.all()

print(all_data)

for row in all_data:
    print(f"\nContent ID : {row.c_id},"
          f"\nTitle : {row.title},"
          f"\nContent : {row.content},"
          f"\nUser ID : {row.id}")
