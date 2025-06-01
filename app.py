from flask import Flask, request
from webhook_handler import handle_update  # 👈 добавлено

app = Flask(__name__)

@app.route('/')
def index():
    return "Functional Body Bot is live."

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    handle_update(data)  # 👈 заменили print
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
