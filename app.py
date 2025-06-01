from flask import Flask, request
from webhook_handler import handle_update

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.get_json()
        handle_update(data)
        return 'OK'