import requests
from main_v1 import get_start_message, get_help_message, get_menu_message

TOKEN = 'AAHtkex3XNgOko_H8MafcCwHNYQrjunmiv4'  # твой токен
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def send_message(chat_id, text):
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(URL, json=payload)

def handle_update(data):
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        if text == '/start':
            send_message(chat_id, get_start_message())
        elif text == '/help':
            send_message(chat_id, get_help_message())
        elif text == '/menu':
            send_message(chat_id, get_menu_message())
        else:
            send_message(chat_id, 'Принято!')