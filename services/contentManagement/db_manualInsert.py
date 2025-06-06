from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Content.db'
db = SQLAlchemy(app)


class Content(db.Model):
    c_id = db.Column(db.String(20), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text())
    id = db.Column(db.String(160))


# Create an instance of the Content model
new_content = Content(
    c_id='5',
    title='Example Title',
    content='Example Content',
    id='456'
)

# Add the new content to the session and commit the changes to the database
with app.app_context():
    db.session.add(new_content)
    db.session.commit()
