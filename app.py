# app.py

from flask import Flask, jsonify, request
from config import Config
from models import db, Student, Course, Lecturer
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Use app.app_context() to initialize the database
with app.app_context():
    db.create_all()

# Routes to handle adding records
@app.route('/lecturers', methods=['POST'])
def add_lecturer():
    data = request.get_json()
    try:
        new_lecturer = Lecturer(name=data['name'])
        db.session.add(new_lecturer)
        db.session.commit()
        return jsonify({'id': new_lecturer.id, 'name': new_lecturer.name}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Lecturer with this name already exists.'}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/courses', methods=['POST'])
def add_course():
    data = request.get_json()
    try:
        new_course = Course(title=data['title'], lecturer_id=data['lecturer_id'])
        db.session.add(new_course)
        db.session.commit()
        return jsonify({'id': new_course.id, 'title': new_course.title}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Course with this title already exists or invalid lecturer ID.'}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    try:
        new_student = Student(name=data['name'], email=data['email'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'id': new_student.id, 'name': new_student.name, 'email': new_student.email}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Student with this email already exists.'}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
