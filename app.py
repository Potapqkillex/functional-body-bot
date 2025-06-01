from flask import Flask, request
from webhook_handler import handle_update

app = Flask(__name__)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    handle_update(data)
    return "ok", 200

@app.route("/", methods=["GET"])
def index():
    return "Бот работает", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)