import requests

BOT_TOKEN = "6661262923:AAGdfRUuLWEyaePL7ZZrU_4J7TZ89UUt8i8"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_message(chat_id, text):
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(API_URL, json=payload)

def handle_update(data):
    if "message" not in data:
        return

    message = data["message"]
    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    if text == "/start":
        send_message(chat_id, "Добро пожаловать в FUNCTIONAL BODY BOT. Используй /menu")
    elif text == "/help":
        send_message(chat_id, "Я функциональный бот. Доступны команды: /start /help /menu")
    elif text == "/menu":
        send_message(chat_id, "Меню:\n1. Тренировки\n2. Питание\n3. Восстановление\n4. Сон\n5. Вода\n6. Мотивация")
    else:
        send_message(chat_id, "Принято!")