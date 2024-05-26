import json


def get_data(filename):
    """Получает путь к файлу формата .json, возвращает данные понятные Python"""
    with open(filename, 'r', encoding='utf-8') as file:
        json_data = file.read()
        data = json.loads(json_data)
    return data


def get_user_level(level, question_liist):
    """Принимает выбор уровня пользователя и список с вопросами,
    возвращаетвопросы согласно выбора пользователя"""
    if level == 'средний':
        words = question_liist[1]
    elif level == 'сложный':
        words = question_liist[2]
    else:
        words = question_liist[0]
    return words


def base_program(words):
    """"""