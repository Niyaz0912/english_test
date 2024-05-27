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


def base_program(questions):
    """функция принимает словарь с вопросами, задает их, получает ответы
    в зависимости от ответов заполняет словарь, который и возвращает"""
    answers = {}

    for word, translate in questions.items():
        answer = input(f"\n{word}, {len(translate)} букв, начинается на {translate[0].upper()}...\n").lower()

        if answer == translate:
            print(f"Верно! {word.title()} это {translate.title()}.")
            answers[word] = True
        else:
            print(f"Неверно! {word.title()} это {translate.title()}.")
            answers[word] = False

    return answers