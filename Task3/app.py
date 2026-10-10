
from flask import Flask, render_template, abort

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 55000,
        "image": "laptop.jpg",
        "description": "A powerful laptop for programming, office work, and study.",
        "category": "Electronics"
    },
    {
        "id": 2,
        "name": "Smartphone",
        "price": 25000,
        "image": "phone.jpg",
        "description": "A modern smartphone with a high-quality display and camera.",
        "category": "Electronics"
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 2500,
        "image": "headphones.jpg",
        "description": "Comfortable headphones for music, calls, and online classes.",
        "category": "Accessories"
    }
]


@app.route("/")
def product_list():
    return render_template(
        "products.html",
        products=products
    )


@app.route("/product/<int:product_id>")
def product_details(product_id):
    product = next(
        (item for item in products if item["id"] == product_id),
        None
    )

    if product is None:
        abort(404)

    return render_template(
        "product_details.html",
        product=product
    )


if __name__ == "__main__":
    app.run(debug=True,port=5003)
