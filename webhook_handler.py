import requests

TOKEN = "6598261864:AAHzcygKzCyGfKhpJrUPVmbCqJAjPu1RT58"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"


def handle_update(update):
    if "message" not in update:
        return

    message = update["message"]
    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    if text == "/start":
        send_message(chat_id, "Добро пожаловать в FUNCTIONAL BODY BOT.\nВведи /menu чтобы увидеть доступные разделы.")
    elif text == "/help":
        send_message(chat_id, "Это функциональный бот. Используй команды:\n/start — запустить бота\n/help — помощь\n/menu — показать меню")
    elif text == "/menu":
        send_message(chat_id, "Меню:\n1. 🏋️‍♂️ Тренировки\n2. 🍽 Питание\n3. ♻️ Восстановление\n4. 🧠 Мотивация\n5. ⚙️ Настройки")
    else:
        send_message(chat_id, "Принято!")

def send_message(chat_id, text):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(URL, json=payload)