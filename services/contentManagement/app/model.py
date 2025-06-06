from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Content(db.Model):
    c_id = db.Column(db.String(20), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text())
    id = db.Column(db.String(160))
