
from flask import Flask, render_template, abort

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "Wings of Fire",
        "author": "A. P. J. Abdul Kalam",
        "year": 1999,
        "description": (
            "An autobiography of A. P. J. Abdul Kalam "
            "about his life, education, and achievements."
        )
    },
    {
        "id": 2,
        "title": "The Guide",
        "author": "R. K. Narayan",
        "year": 1958,
        "description": (
            "A novel about Raju and his transformation "
            "from a tour guide into a spiritual guide."
        )
    },
    {
        "id": 3,
        "title": "Ponniyin Selvan",
        "author": "Kalki Krishnamurthy",
        "year": 1950,
        "description": (
            "A famous Tamil historical novel set during "
            "the Chola dynasty."
        )
    },
    {
        "id": 4,
        "title": "The Discovery of India",
        "author": "Jawaharlal Nehru",
        "year": 1946,
        "description": (
            "A book exploring India's history, culture, "
            "and philosophical traditions."
        )
    },
    {
        "id": 5,
        "title": "Thirukkural",
        "author": "Thiruvalluvar",
        "year": None,
        "description": (
            "A classical Tamil text containing couplets "
            "on virtue, wealth, and love. Its exact "
            "composition date is uncertain."
        )
    }
]


@app.route("/")
def home():
    return render_template("home.html", books=books)


@app.route("/books")
def book_list():
    return render_template("books.html", books=books)


@app.route("/book/<int:book_id>")
def book_details(book_id):
    book = next(
        (item for item in books if item["id"] == book_id),
        None
    )

    if book is None:
        abort(404)

    return render_template(
        "book_details.html",
        book=book
    )


if __name__ == "__main__":
    app.run(debug=True,port=5008)
