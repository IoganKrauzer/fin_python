"""Задача 2:
� Создайте модуль с функцией внутри.
� Функция получает на вход загадку, список с возможными
вариантами отгадок и количество попыток на угадывание.

"""

from random import choice
from sys import argv
import logging


def game_riddle(riddle_text, answer_list_, attempts_):
    answer_list_ = list(map(lambda ans: ans.lower(), answer_list_))
    count = 0
    user_answers = []
    player_name = input('Введите имя игрока: ')
    print(riddle_text)
    while count < attempts_:
        answer = input("Введите отгадку: ")
        user_answers.append(answer)
        count += 1
        if answer.lower() in answer_list_:
            logger_text = f'Игрок {player_name} - выиграл. Ответы игрока: {user_answers} Угадал с {count} попытки'
            logger.info(logger_text)
            print(f"Вы угадали! Попытка номер {count}")
            break
        else:
            print(f'Попробуйте еще раз! Попыток осталось: {attempts_ - count}')
    else:
        logger_text = f'Игрок {player_name} - проиграл. Все попытки исчерпаны. Ответы игрока: {user_answers}'
        logger.info(logger_text)
        print(f"Попытки закончились. Правильный ответ {choice(answer_list)}")


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='task_2.txt', filemode='a', encoding='utf-8', level=logging.INFO)
    argv_ = argv[1]
    if argv_ == '/start':
        riddle = 'Зимой и летом одним цветом?'
        answer_list = ['ель', 'елка', 'елочка']
        attempts = 3
        game_riddle(riddle, answer_list, attempts)
    else:
        logger.error(f'Wrong command {argv_} Try to write /start')


