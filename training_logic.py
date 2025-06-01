# training_logic.py

def get_training_response(goal, level, location):
    if goal == "Сила":
        if level == "Начальный":
            return "Тренировка на силу для начального уровня (дом): 3 подхода отжиманий, 3 приседа, 3 планки по 30 сек."
        elif level == "Средний":
            return "Силовая тренировка среднего уровня (зал): жим лежа, тяга, присед — по 4 подхода."
        else:
            return "Продвинутая силовая (зал): комплекс из 5 силовых упражнений с прогрессией."
    elif goal == "Гибкость":
        return "Тренировка на гибкость: 20 минут работы над шпагатом и раскрытием таза."
    else:
        return "Тренировка под задачу загружается. Скоро будет доступна."

def parse_training_command(message_text):
    parts = message_text.split(",")
    if len(parts) == 3:
        goal = parts[0].strip()
        level = parts[1].strip()
        location = parts[2].strip()
        return get_training_response(goal, level, location)
    else:
        return "Формат запроса: 'Сила, Начальный, Дом'"
