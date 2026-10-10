
from flask import Flask, render_template, abort

app = Flask(__name__)

profile = {
    "name": "Gowtham Kumar",
    "role": "Python Flask Developer",
    "email": "gowtham@example.com",
    "location": "Tamil Nadu, India",
    "bio": (
        "I am a developer learning Python, Flask, "
        "web development, and database management."
    ),
    "skills": ["Python", "Flask", "HTML", "CSS", "MySQL"]
}

projects = [
    {
        "id": 1,
        "name": "Student Management System",
        "category": "Web Development",
        "status": "Completed",
        "description": (
            "A web application to manage student details, "
            "courses, and student records using Flask."
        ),
        "technologies": ["Python", "Flask", "HTML", "CSS"]
    },
    {
        "id": 2,
        "name": "Library Management System",
        "category": "Web Development",
        "status": "In Progress",
        "description": (
            "A library application to display books, "
            "authors, publication years, and book details."
        ),
        "technologies": ["Python", "Flask", "Jinja2"]
    },
    {
        "id": 3,
        "name": "Job Portal",
        "category": "Full Stack Development",
        "status": "Planned",
        "description": (
            "A job portal where users can browse jobs "
            "and view company, location, and salary details."
        ),
        "technologies": ["Python", "Flask", "HTML", "CSS"]
    },
    {
        "id": 4,
        "name": "Personal Portfolio",
        "category": "Portfolio",
        "status": "Completed",
        "description": (
            "A portfolio website presenting personal "
            "information, technical skills, and projects."
        ),
        "technologies": ["HTML", "CSS", "Flask"]
    }
]


@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        profile=profile,
        projects=projects
    )


@app.route("/profile")
def user_profile():
    return render_template(
        "profile.html",
        profile=profile
    )


@app.route("/projects")
def project_list():
    return render_template(
        "projects.html",
        projects=projects
    )


@app.route("/project/<int:project_id>")
def project_details(project_id):
    project = next(
        (item for item in projects
         if item["id"] == project_id),
        None
    )

    if project is None:
        abort(404)

    return render_template(
        "project_details.html",
        project=project
    )


if __name__ == "__main__":
    app.run(debug=True,port=5010)
