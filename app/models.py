from . import db
from datetime import datetime

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    id_number = db.Column(db.String(50))
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    area = db.Column(db.String(50))

    def __repr__(self):
        return f"<Student {self.name}>"