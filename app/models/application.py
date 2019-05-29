from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Labs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lab_type = db.Column(db.String(10), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    course = db.Column(db.String(20), nullable=False)

