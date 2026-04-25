from flask import Flask, jsonify, request
import os

app = Flask(__name__)

items = [{"name": "item1"}]

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "env": os.getenv("APP_ENV", "dev")
    }), 200

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items), 200

@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json(silent=True) or {}
    if "name" not in data:
        return jsonify({"error": "missing name"}), 400
    items.append(data)
    return jsonify({"message": "item added", "item": data}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
