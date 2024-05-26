from utils.utils import get_data

questions, levels = get_data('questions_data/questions.json')
questions_list = questions['questions']
knowledge_level = levels ['levels']
user_name = input("Введите Ваше имя: ")