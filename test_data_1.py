import re
import random


# Длинные ответы
Answer = ["Меня зовут Ангелина компания диджитал бизнес звоним вам по поводу продления лицензии",
          "Добрый день, меня Максим зовут компания китобизнес",
          "Да, это Анастасия"][random.randrange(3)]
Answer_2 = ["Меня зовут Ангелина компания диджитал бизнес звоним вам по поводу продления лицензии",
          "Добрый день, меня Максим зовут компания китобизнес",
          "Да, это Анастасия"][random.randrange(3)]


# Функция возвращает неопознаннные ответы
def unknown():
    response = ["Можете, пожалуйста, повторить?",
                "...",
                "Не совсем понимаю вас",
                "Что вы имеете в виду?"][random.randrange(4)]
    return response




# Функция вычисляет вероятность ответов в сообщении
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True


    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

# Функция проверяет сообщения
def check_all_messages(message):
    highest_prob_list = {}


    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Здравствуйте', ['алло', 'привет', 'здравствуйте', 'добрый день', 'добрый вечер', 'добрый'], single_response=True)
    response('До свидания', ['досвидания', 'пока', 'до встречи', 'увидимся', 'бай', 'гуд бай', 'прощайте', 'всего хорошего', 'давайте'], single_response=True)
    response(Answer, ['кто', 'это', 'мне', 'звонит'], required_words=['кто'])
    response(Answer_2, ['как', 'вас', 'зовут'], required_words=['как'])




    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)

    return unknown() if highest_prob_list[best_match] < 1 else best_match




# Функция делит слова от знаков
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response



# Тестирует систему вопрос-ответ
while True:
    print(f'Менеджер: ' + get_response(input('Клиент:  ') ))
