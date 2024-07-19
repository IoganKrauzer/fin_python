"""� Создайте модуль с функцией внутри.
� Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
� Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
� Функция выводит подсказки “больше” и “меньше”.
� Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь.
"""
from pathlib import Path
from random import randint as rnd
from sys import argv
import logging


def find_func(start, stop, count):

    gues_number = rnd(start, stop)
    for k in range(1, count + 1):
        check_num = int(input('Введите число для угадывания: '))
        if check_num == gues_number:
            print('Угадали!')
            print(gues_number)
            logger_text = f'{gues_number = }; result: Win'
            logger.info(logger_text)
            return True
        elif check_num < gues_number:
            print('Больше!')
            print(f'Осталось попыток: {count - k}')
        else:
            print('Меньше!')
            print(f'Осталось попыток: {count - k}')
    else:
        print('Вы исчерпали все попытки!')
        print(f'Загаданное число: {gues_number}!')
        logger_text = f'{gues_number = }; result: Loose'
        logger.info(logger_text)
        return False


def check_argv(argv_):
    try:
        argv_ = list(map(int, argv_))

    except ValueError as e:
        logging.error(e)
    return argv_


if __name__ == '__main__':

    # print(Path.cwd())
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='task_3.txt', filemode='a', encoding='utf-8', level=logging.INFO)
    start, stop, count = 1, 10, 3
    argv = argv[1:]
    argv = check_argv(argv)
    # argv = list(map(int, argv[1:]))
    match argv:
        case [stop]:
            stop = argv[0]
        case [start, stop]:
            start, stop = argv[0:]
        case [start, stop, count]:
            start, stop, count = argv[0:]

    find_func(start, stop, count)


