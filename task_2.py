"""Задача 2:
� Создайте модуль с функцией внутри.
� Функция получает на вход загадку, список с возможными
вариантами отгадок и количество попыток на угадывание.

"""

from random import choice
import argparse
import logging


def game_riddle(riddle_text, answer_list_, attempts_):
    counter = 0
    user_answers = []
    print(riddle_text)
    while counter < attempts_:
        counter += 1
        answer = (input('Введите отгадку: ')).lower()
        user_answers.append(answer)
        if answer in answer_list_:
            logger_text = f'Игрок {args.name} - выиграл. Ответы игрока: {user_answers} Угадал с {counter} попытки' \
                          f' | Правильный ответ: {answer}'
            logger.info(logger_text)
            print(f"Вы угадали! Попытка номер {counter}")
            break
        else:
            print(f'Попробуйте еще раз! Попыток осталось: {attempts_ - counter}')
    else:
        logger_text = f'Игрок {args.name} - проиграл. Все попытки исчерпаны. Ответы игрока: {user_answers}'
        logger.info(logger_text)
        print(f"Попытки закончились. Правильный ответ {choice(answer_list)}")


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='task_2.txt', filemode='a', encoding='utf-8', level=logging.INFO)

    riddle = 'Зимой и летом одним цветом?'
    answer_list = ['ель', 'елка', 'елочка']
    attempts = 3
    parser = argparse.ArgumentParser(
        description='"Отгадайка". Пользователю выдает текст загадки. Пользователь должен ввести ответ кириллицей')
    parser.add_argument('-n', '--name', help='Имя игрока', type=str, default='User')
    parser.add_argument('-r', '--riddle', help='Загадка', type=str, default=riddle)
    parser.add_argument('-a', '--answer', help='Ответы', type=str, nargs='+', default=answer_list)
    parser.add_argument('-c', '--count', help='Попытки', type=int, default=3)
    args = parser.parse_args()
    game_riddle(args.riddle, args.answer, args.count)


