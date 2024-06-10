from utils.utils import get_data, get_user_level, base_program, get_result, write_answers

questions, levels = get_data('questions_data/questions.json')
questions_list = questions['questions']
knowledge_level = levels ['levels']
user_name = input("Введите Ваше имя: ")
user_level = input("Выберите уровень сложности легкий/средний/сложный: ")
user_questions = get_user_level(user_level, questions_list)
user_answers = base_program(user_questions)
user_result = get_result(user_answers, knowledge_level)
print(write_answers(fr'sudents_data/{user_name}_answers.json', user_answers))