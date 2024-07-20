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

from random import randint as rnd
import logging
import argparse


def find_func(start, stop, count):
    gues_number = rnd(start, stop)
    lst_pl_answers = []
    args.player_name = input('Введите имя игрока: ')
    for k in range(1, count + 1):
        while True:
            try:
                args.check_num = input('Введите число для угадывания: ')
                lst_pl_answers.append(args.check_num)
                args.check_num = int(args.check_num)
                break
            except ValueError:
                print(f'{args.player_name}, надо ввести целочисленное число')
                logger.error(f'{args.player_name} ввел {args}')
        lst_pl_answers.append(args.check_num)
        if args.check_num == gues_number:
            print('Угадали!')
            print(gues_number)
            logger_text = f'Игрок: {args.player_name} Загаданное число: {gues_number} | '\
                          f'result: Win | Ответы игрока: {lst_pl_answers} | Параметры игры: {args}'
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
        logger_text = f'Игрок: {args.player_name} Загаданное число: {gues_number} | ' \
                      f'result: Loose | Ответы игрока: {lst_pl_answers} | Параметры игры: {args}'
        logger.info(logger_text)
        return False


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='task_3.txt', filemode='a', encoding='utf-8', level=logging.INFO)

    parser = argparse.ArgumentParser(
        description='Создается диапазон чисел для игры "Угадайка" и количество попыток')
    parser.add_argument('-s', '--start', help='Нижняя граница', type=int)
    parser.add_argument('-f', '--stop', help='Верхняя граница ', type=int)
    parser.add_argument('-c', '--count', help='Количество попыток', type=int)
    args = parser.parse_args()
    find_func(args.start, args.stop, args.count)

