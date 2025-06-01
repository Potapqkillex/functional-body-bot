import requests

TOKEN = '7179411906:AAHtkezX3Ng0ko_H8MafcCwHNYQrjunmiv4'

def handle_update(data):
    print("Handling update:", data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            reply = "Добро пожаловать в Functional Body Bot 👊"
            keyboard = {
                "keyboard": [[{"text": "Мой рацион"}, {"text": "Моя тренировка"}]],
                "resize_keyboard": True
            }
            send_message(chat_id, reply, keyboard)
        else:
            reply = "Принято!"
            send_message(chat_id, reply)


def send_message(chat_id, text, reply_markup=None):
    payload = {
        "chat_id": chat_id,
        "text": text
    }

    if reply_markup:
        payload["reply_markup"] = reply_markup

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json=payload
    )