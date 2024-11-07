from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Note(db.Model):
    __tablename__ = "notee_notes"
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(20))
    username = db.Column(db.String(), nullable=False)
    title = db.Column(db.String(50), unique=True)
    description = db.Column(db.String())
    comment = db.Column(db.String())

    def __init__(self, ip_address, username, title, description, comment):
        self.ip_address = ip_address
        self.username = username
        self.title = title
        self.description = description
        self.comment = comment

