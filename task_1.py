import logging

"""
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""
import logging
import argparse


def create_dict_for_chr_ord(numbers_):
    start, stop = sorted(numbers_)
    if stop - start > RANGE_BORDER:
        logger.error('Вы превысили заданный диапазон')
        return 0
    logger_text = f'Пользователь {args.user} задал диапазон от {start} до {stop}'
    logger.info(logger_text)
    return {chr(i): i for i in range(start, stop + 1)}


def show_dict(dict_):
    for items, value in dict_.items():
        print(f'{items} = {value}')


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='task_1.txt', filemode='a', encoding='utf-8', level=logging.INFO)
    RANGE_BORDER = 75
    def_num = [65, 122]
    parser = argparse.ArgumentParser(
        'Пользователь передает два параметра. Программа создает словарь. '
        'Ключом является символ в Unicode, а значением его число в Unicode')
    parser.add_argument('-u', '--user', help='имя пользователя', type=str, default='User')
    parser.add_argument('-n', '--numbers', nargs='+', help='введите два числа', default=def_num,
                        type=int)

    args = parser.parse_args()
    show_dict(create_dict_for_chr_ord(args.numbers))
