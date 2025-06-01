from flask import Flask, request
from webhook_handler import handle_update

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running."

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    handle_update(data)
    return '', 200