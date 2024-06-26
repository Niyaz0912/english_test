from utils.utils import get_data, get_user_level, base_program, get_result, write_answers

questions, levels = get_data(r'questions_data/questions.json')
questions_list = questions['questions']
knowledge_level = levels['levels']
user_name = input("Введите свое имя: ")
user_level = input("Введите уровень сложности легкий/средний/сложный: ")
user_words = get_user_level(user_level, questions_list)
user_answers = base_program(user_words)
user_result = get_result(user_answers, knowledge_level)
print(f"\nВаш ранг:\n{user_result}")
write_answers(fr'students_data/{user_name}_answers.json', user_answers)