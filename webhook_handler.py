import requests
from training_logic import parse_training_command
BOT_TOKEN = "7179411906:AAHtkezX3Ng0ko_H8MafcCwHNYQrjunmiv4"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_message(chat_id, text, reply_markup=None):
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML'
    }
    if reply_markup:
        payload['reply_markup'] = reply_markup
    requests.post(f"{API_URL}/sendMessage", json=payload)

def handle_update(data):
    if "message" in data:
        message = data["message"]
        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        if text == "/start":
            send_message(chat_id, "Добро пожаловать в FUNCTIONAL BODY BOT. Используй /menu")
        elif text == "/help":
            send_message(chat_id, "Я функциональный бот. Доступны команды: /start /help /menu")
        elif text == "/menu":
            keyboard = {
                "inline_keyboard": [
                    [{"text": "Тренировки", "callback_data": "trainings"}],
                    [{"text": "Питание", "callback_data": "nutrition"}],
                    [{"text": "Восстановление", "callback_data": "recovery"}],
                    [{"text": "Сон", "callback_data": "sleep"}],
                    [{"text": "Вода", "callback_data": "water"}],
                    [{"text": "Мотивация", "callback_data": "motivation"}],
                ]
            }
            send_message(chat_id, "Выбери раздел:", reply_markup=keyboard)
        else:
            send_message(chat_id, "Принято!")

    elif "callback_query" in data:
        callback = data["callback_query"]
        chat_id = callback["message"]["chat"]["id"]
        data = callback["data"]

        responses = {
            "trainings": "Раздел 'Тренировки' скоро будет активен.",
            "nutrition": "Раздел 'Питание' скоро будет активен.",
            "recovery": "Раздел 'Восстановление' скоро будет активен.",
            "sleep": "Раздел 'Сон' скоро будет активен.",
            "water": "Раздел 'Вода' скоро будет активен.",
            "motivation": "Раздел 'Мотивация' скоро будет активен.",
        }

        text = responses.get(data, "В разработке...")
        send_message(chat_id, text)