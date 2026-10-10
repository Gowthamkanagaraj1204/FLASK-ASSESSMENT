
from flask import Flask, render_template, abort

app = Flask(__name__)

employees = {
    "gowtham": {
        "name": "Gowtham Kumar",
        "username": "gowtham",
        "role": "Python Flask Developer",
        "email": "gowtham@example.com",
        "location": "Tamil Nadu, India",
        "about": "I am a passionate developer interested in Python, Flask, web development, and database management.",
        "skills": ["Python", "Flask", "HTML", "CSS", "JavaScript", "MySQL"],
        "image": "profile.jpg"
    },
    "arun": {
        "name": "Arun Kumar",
        "username": "arun",
        "role": "Frontend Developer",
        "email": "arun@example.com",
        "location": "Chennai, India",
        "about": "I enjoy building responsive and user-friendly websites.",
        "skills": ["HTML", "CSS", "JavaScript", "Bootstrap"],
        "image": "profile.jpg"
    }
}


@app.route("/")
def home():
    return render_template(
        "home.html",
        employees=employees.values()
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/employee/<username>")
def employee_profile(username):
    employee = employees.get(username.lower())

    if employee is None:
        abort(404)

    return render_template(
        "employee.html",
        employee=employee
    )


if __name__ == "__main__":
    app.run(debug=True,port=5001)
 