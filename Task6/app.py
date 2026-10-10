
from flask import Flask, render_template, abort

app = Flask(__name__)

foods = [
    {
        "id": 1,
        "name": "Chicken Biryani",
        "price": 220,
        "image": "biryani.jpg",
        "category": "Main Course",
        "description": "Aromatic basmati rice cooked with chicken and traditional spices.",
        "type": "Non-Vegetarian"
    },
    {
        "id": 2,
        "name": "Margherita Pizza",
        "price": 180,
        "image": "pizza.jpg",
        "category": "Fast Food",
        "description": "Classic pizza topped with tomato sauce, cheese, and herbs.",
        "type": "Vegetarian"
    },
    {
        "id": 3,
        "name": "Veg Burger",
        "price": 120,
        "image": "burger.jpg",
        "category": "Fast Food",
        "description": "A tasty vegetable patty burger served with fresh vegetables.",
        "type": "Vegetarian"
    },
    {
        "id": 4,
        "name": "Masala Dosa",
        "price": 90,
        "image": "dosa.jpg",
        "category": "South Indian",
        "description": "Crispy dosa filled with spiced potato masala.",
        "type": "Vegetarian"
    }
]


@app.route("/")
def home():
    return render_template("home.html", foods=foods)


@app.route("/menu")
def menu():
    return render_template("menu.html", foods=foods)


@app.route("/food/<int:food_id>")
def food_details(food_id):
    food = next(
        (item for item in foods if item["id"] == food_id),
        None
    )

    if food is None:
        abort(404)

    return render_template("food_details.html", food=food)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True,port=5006)
