from flask import Flask, request
from webhook_handler import handle_update, TOKEN

app = Flask(__name__)

@app.route('/')
def index():
    return 'Бот работает!'

@app.route(f'/{TOKEN}', methods=["POST"])
def webhook():
    data = request.get_json()
    handle_update(data)
    return '', 200