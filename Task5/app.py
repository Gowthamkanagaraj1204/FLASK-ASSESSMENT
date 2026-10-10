
from flask import Flask, render_template, abort

app = Flask(__name__)

posts = [
    {
        "id": 1,
        "title": "Introduction to Python",
        "author": "Gowtham Kumar",
        "summary": "Learn the basics of Python programming.",
        "content": """
Python is a popular programming language known for its
simple syntax and readability.

It is used in web development, automation, data science,
artificial intelligence, and many other fields.

Beginners can start with variables, data types, conditions,
loops, functions, and object-oriented programming.
""",
        "date": "10 October 2026"
    },
    {
        "id": 2,
        "title": "Getting Started with Flask",
        "author": "Arun Kumar",
        "summary": "Discover how to build web applications using Flask.",
        "content": """
Flask is a lightweight Python web framework.

It helps developers create web applications using routes,
HTML templates, request handling, and Jinja2.

You can organize your application using templates and
static files, and connect it to a database when needed.
""",
        "date": "9 October 2026"
    },
    {
        "id": 3,
        "title": "Why Learn SQL?",
        "author": "Priya",
        "summary": "Understand how SQL helps manage databases.",
        "content": """
SQL stands for Structured Query Language.

It is used to create, retrieve, update, and delete data
in relational databases such as MySQL and SQLite.

Important SQL topics include SELECT queries, filtering,
joins, aggregate functions, and constraints.
""",
        "date": "8 October 2026"
    }
]


@app.route("/")
def home():
    return render_template("home.html", posts=posts)


@app.route("/blogs")
def blog_list():
    return render_template("blogs.html", posts=posts)


@app.route("/blog/<int:post_id>")
def blog_detail(post_id):
    post = next(
        (item for item in posts if item["id"] == post_id),
        None
    )

    if post is None:
        abort(404)

    return render_template("blog_detail.html", post=post)


if __name__ == "__main__":
    app.run(debug=True,port=5005)
