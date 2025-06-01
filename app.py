from flask import Flask, request
from webhook_handler import handle_update

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    handle_update(data)
    return '', 200

if __name__ == '__main__':
    app.run()