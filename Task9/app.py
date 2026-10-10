
from flask import Flask, render_template, abort

app = Flask(__name__)

jobs = [
    {
        "id": 1,
        "title": "Python Developer",
        "company": "Tech Solutions",
        "location": "Chennai, Tamil Nadu",
        "salary": "₹4,00,000 - ₹7,00,000 per year",
        "type": "Full-time",
        "description": (
            "Develop Python applications, build APIs, "
            "and maintain backend services."
        ),
        "skills": ["Python", "Flask", "SQL", "Git"]
    },
    {
        "id": 2,
        "title": "Web Developer",
        "company": "Creative Web Pvt Ltd",
        "location": "Bengaluru, Karnataka",
        "salary": "₹3,50,000 - ₹6,00,000 per year",
        "type": "Full-time",
        "description": (
            "Build responsive websites using HTML, CSS, "
            "JavaScript, and backend technologies."
        ),
        "skills": ["HTML", "CSS", "JavaScript", "Python"]
    },
    {
        "id": 3,
        "title": "Data Analyst",
        "company": "Data Insights",
        "location": "Coimbatore, Tamil Nadu",
        "salary": "₹3,00,000 - ₹5,50,000 per year",
        "type": "Full-time",
        "description": (
            "Analyze datasets, create reports, and "
            "communicate business insights."
        ),
        "skills": ["Python", "SQL", "Excel", "Power BI"]
    },
    {
        "id": 4,
        "title": "Junior Software Engineer",
        "company": "NextGen Technologies",
        "location": "Hyderabad, Telangana",
        "salary": "₹3,50,000 - ₹6,50,000 per year",
        "type": "Full-time",
        "description": (
            "Assist in software development, testing, "
            "debugging, and application maintenance."
        ),
        "skills": ["Python", "OOP", "SQL", "Git"]
    }
]


@app.route("/")
def home():
    return render_template("home.html", jobs=jobs)


@app.route("/jobs")
def job_listings():
    return render_template("jobs.html", jobs=jobs)


@app.route("/job/<int:job_id>")
def job_details(job_id):
    job = next(
        (item for item in jobs if item["id"] == job_id),
        None
    )

    if job is None:
        abort(404)

    return render_template("job_details.html", job=job)


if __name__ == "__main__":
    app.run(debug=True,port=5009)
