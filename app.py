from flask import Flask, request, jsonify

app = Flask(__name__)

# Example endpoint: GET /price?product=Logitech Pebble Mouse
@app.route("/price", methods=["GET"])
def get_price():
    product = request.args.get("product")

    # ✅ TODO: Replace this with Amazon & Flipkart API calls
    # For now, returning dummy response
    response = {
        "product": product,
        "amazon": {
            "price": "₹1,299",
            "url": "https://www.amazon.in/example"
        },
        "flipkart": {
            "price": "₹1,249",
            "url": "https://www.flipkart.com/example"
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
