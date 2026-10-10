
from flask import Flask, render_template, abort

app = Flask(__name__)

courses = [
    {
        "id": 1,
        "name": "Python Programming",
        "slug": "python-programming",
        "category": "Programming",
        "duration": "6 weeks",
        "price": 1999,
        "image": "python.jpg",
        "description": "Learn Python from the basics to advanced concepts.",
        "topics": ["Variables", "Loops", "Functions", "OOP", "File Handling"]
    },
    {
        "id": 2,
        "name": "Flask Web Development",
        "slug": "flask-web-development",
        "category": "Web Development",
        "duration": "4 weeks",
        "price": 2499,
        "image": "flask.jpg",
        "description": "Build web applications using Flask and Jinja2.",
        "topics": ["Routes", "Templates", "Forms", "Static Files", "CRUD"]
    },
    {
        "id": 3,
        "name": "MySQL Database",
        "slug": "mysql-database",
        "category": "Database",
        "duration": "3 weeks",
        "price": 1499,
        "image": "sql.jpg",
        "description": "Learn how to design databases and write SQL queries.",
        "topics": ["DDL", "DML", "Joins", "Functions", "Constraints"]
    }
]


@app.route("/")
def home():
    return render_template("home.html", courses=courses)


@app.route("/courses")
def course_list():
    return render_template("courses.html", courses=courses)


@app.route("/course/<int:course_id>")
def course_details(course_id):
    course = next(
        (item for item in courses if item["id"] == course_id),
        None
    )

    if course is None:
        abort(404)

    return render_template("course_details.html", course=course)


@app.route("/course/name/<slug>")
def course_by_name(slug):
    course = next(
        (item for item in courses if item["slug"] == slug),
        None
    )

    if course is None:
        abort(404)

    return render_template("course_details.html", course=course)


if __name__ == "__main__":
    app.run(debug=True,port=5004)
