
from flask import Flask, render_template, abort

app = Flask(__name__)

destinations = [
    {
        "name": "Taj Mahal",
        "slug": "taj-mahal",
        "location": "Agra, Uttar Pradesh",
        "description": (
            "The Taj Mahal is a famous white marble monument "
            "and one of India's most popular tourist attractions."
        ),
        "image": "images/taj-mahal.jpg"
    },
    {
        "name": "Ooty",
        "slug": "ooty",
        "location": "Nilgiris, Tamil Nadu",
        "description": (
            "Ooty is a beautiful hill station known for its "
            "tea gardens, botanical gardens, and cool climate."
        ),
        "image": "images/ooty.jpg"
    },
    {
        "name": "Kanyakumari",
        "slug": "kanyakumari",
        "location": "Tamil Nadu",
        "description": (
            "Kanyakumari is famous for its coastal scenery, "
            "Vivekananda Rock Memorial, and sunrise views."
        ),
        "image": "images/kanyakumari.jpg"
    },
    {
        "name": "Jaipur",
        "slug": "jaipur",
        "location": "Rajasthan",
        "description": (
            "Jaipur, the Pink City, is known for its historic "
            "forts, palaces, and colourful markets."
        ),
        "image": "images/jaipur.jpg"
    }
]


@app.route("/")
def home():
    return render_template(
        "home.html",
        destinations=destinations
    )


@app.route("/destination/<slug>")
def destination_details(slug):
    destination = next(
        (item for item in destinations
         if item["slug"] == slug),
        None
    )

    if destination is None:
        abort(404)

    return render_template(
        "destination_details.html",
        destination=destination
    )


if __name__ == "__main__":
    app.run(debug=True,port=5007)
