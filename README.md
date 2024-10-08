
# Flask School App - Initial Version

This is the first version of a simple **School Management API** built using **Flask** and **Flask-SQLAlchemy**. This API allows you to manage data for students, courses, and lecturers with basic validation for input data.

## Features

- **Add Lecturers**: Create new lecturers with unique names.
- **Add Courses**: Create courses associated with a lecturer.
- **Add Students**: Create students with unique emails.
- **Validation**: Input validation ensures that names, emails, and course titles meet length and uniqueness constraints.

## Prerequisites

Before running this application, you need to have the following installed on your machine:

- **Python 3.7+**
- **pip** (Python package manager)
- (Optional but recommended) **Virtualenv** for creating isolated environments

## Installation and Setup

### 1. Clone the Repository

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/KelvinMuriithi/flask-validations-constraints.git
cd flask-validations-constraints
```

### 2. Set Up a Virtual Environment

It is a good practice to use a virtual environment to manage dependencies for this project:

```bash
# For Linux/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Once the virtual environment is activated, install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

This project uses **SQLite** as the default database for simplicity. The database configuration is set in `config.py`:

```python
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///school.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### 5. Run the Application

To start the Flask server, use the following command:

```bash
python app.py
```

This will start the application on `http://127.0.0.1:5000`.

### 6. Create the Database

The database tables can be created automatically when the app starts. Alternatively, you can manually initialize the database with the following commands:

```bash
from app import db
db.create_all()
```




## License

This project is licensed under the MIT License.
