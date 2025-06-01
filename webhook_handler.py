def handle_update(data):
    print("Handling update:", data)

    message = data.get('message')
    if not message:
        return

    chat_id = message['chat']['id']
    text = message.get('text', '')

    # здесь можно добавить любую логику
    print(f"Сообщение от {chat_id}: {text}")