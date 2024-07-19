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
import argparse


def find_func(start, stop, count):
    gues_number = rnd(start, stop)
    lst_pl_answers = []
    args.player_name = input('Введите имя игрока: ')
    for k in range(1, int(count) + 1):
        args.check_num = int(input('Введите число для угадывания: '))
        lst_pl_answers.append(args.check_num)
        if args.check_num == gues_number:
            print('Угадали!')
            print(gues_number)
            logger_text = f'Игрок: {args.player_name} {gues_number = }; result: Win Ответы: {lst_pl_answers}'
            logger.info(logger_text)
            return True
        elif args.check_num < gues_number:
            print('Больше!')
            print(f'Осталось попыток: {count - k}')
        else:
            print('Меньше!')
            print(f'Осталось попыток: {count - k}')
    else:
        print('Вы исчерпали все попытки!')
        print(f'Загаданное число: {gues_number}!')
        logger_text = f'Игрок: {args.player_name} {gues_number = }; result: Loose Ответы игрока: {lst_pl_answers}'
        logger.info(logger_text)
        return False


if __name__ == '__main__':

    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='task_3.txt', filemode='a', encoding='utf-8', level=logging.INFO)

    parser = argparse.ArgumentParser(
        description='Создается диапазон чисел для игры "Угадайка" и количество попыток')
    parser.add_argument('start', help='Нижняя граница')
    parser.add_argument('stop', help='Верхняя граница ')
    parser.add_argument('count', help='Количество попыток')
    args = parser.parse_args()

    find_func(int(args.start), int(args.stop), int(args.count))
