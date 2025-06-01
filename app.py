from flask import Flask, request
from webhook_handler import handle_update, TOKEN
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Бот работает!'

@app.route(f'/{TOKEN}', methods=["POST"])
def webhook():
    data = request.get_json()
    handle_update(data)
    return '', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)