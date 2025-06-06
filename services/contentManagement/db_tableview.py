from app import create_service2
from app.model import db, Content
from sqlalchemy import create_engine, inspect

content_service = create_service2()

# # Assuming you have a Flask app instance and Content model defined
#
# with content_service.app_context():
#     all_tables = db.engine.table_names()
#     print(all_tables)

# Get a list of all tables
with content_service.app_context():
    inspector = inspect(db.engine)
    all_tables = inspector.get_table_names()

# Print the table names
for table in all_tables:
    print(table)
