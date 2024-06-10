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

def get_result(answers, knowledge_level):
    """Функция принимает словарь с ответами пользователя
    и словарь со шкалой оценки знаний, сообщает что верно, а что нет.
    Возвращает уровень знаний пользователя"""

    counter = 0
    print("\nПравильно отвечены слова:")
    for key, value in answers.items():
        if value is True:
            print(key)
            counter += 1
    print("\nНеправильно отвечены слова:")
    for key, value in answers.items():
        if value is False:
            print(key)
    return knowledge_level[str(counter)]

def write_answers(filename, answers):
    """Функция принимает имя файла и словарь с ответами пользователя,
    записывает эти ответы в файл формата .json, возвращает
    соответствующее сообщение"""
    answers_json = json.dumps(answers, ensure_ascii=False, indent=4)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(answers_json)
        return "Ответы записаны"