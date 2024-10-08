# models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Lecturer(db.Model):
    __tablename__ = 'lecturers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    @validates('name')
    def validate_name(self, key, name):
        if not name or len(name) > 50:
            raise ValueError("Lecturer name must be between 1 and 50 characters.")
        return name


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    lecturer_id = db.Column(db.Integer, db.ForeignKey('lecturers.id'), nullable=False)

    @validates('title')
    def validate_title(self, key, title):
        if not title or len(title) > 100:
            raise ValueError("Course title must be between 1 and 100 characters.")
        return title


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

    @validates('name')
    def validate_name(self, key, name):
        if not name or len(name) > 50:
            raise ValueError("Student name must be between 1 and 50 characters.")
        return name

    @validates('email')
    def validate_email(self, key, email):
        if not email or len(email) > 120:
            raise ValueError("Student email must be a valid email format and within 120 characters.")
        return email
