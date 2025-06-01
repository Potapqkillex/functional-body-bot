import requests

# Твой токен Telegram-бота
TOKEN = '7179411906:AAHtkezX3Ng0ko_H8MafcCwHNYQrjunmiv4'

def handle_update(data):
    print("Handling update:", data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # Ответ пользователю
        reply = "Принято!" if text else "Не понял тебя 🤖"

        # Отправка ответа через Telegram API
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": reply}
        )