from flask import Flask, request
import requests

TOKEN = '7179411906:AAHtkezX3Ng0ko_H8MafcCwHNYQrjunmiv4'
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

def get_start_message():
    return "Добро пожаловать в FUNCTIONAL BODY BOT.\nИспользуй /menu для навигации."

def get_help_message():
    return "Это функциональный бот. Используй /menu чтобы выбрать направление."

def get_menu_message():
    return (
        "Меню:\n"
        "1. Тренировки — /training\n"
        "2. Питание — /nutrition\n"
        "3. Восстановление — /recovery"
    )

def get_training_block():
    return "Функциональные тренировки: сила, выносливость, гибкость. Программы — скоро здесь."

def get_nutrition_block():
    return "Питание: КБЖУ, добавки, режим. Следим за балансом."

def get_recovery_block():
    return "Восстановление: сон, дыхание, магний, растяжка. Управление ресурсом."

def handle_update(data):
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            reply = get_start_message()
        elif text == "/help":
            reply = get_help_message()
        elif text == "/menu":
            reply = get_menu_message()
        elif text == "/training":
            reply = get_training_block()
        elif text == "/nutrition":
            reply = get_nutrition_block()
        elif text == "/recovery":
            reply = get_recovery_block()
        else:
            reply = "Принято!"

        requests.post(URL, json={"chat_id": chat_id, "text": reply})
