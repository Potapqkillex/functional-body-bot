from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Functional Body Bot is live."

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Received update: {data}")
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
