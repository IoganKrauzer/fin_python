import logging

"""
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""
import logging
from sys import argv


def create_dict_for_chr_ord():
    start, stop = sorted(map(int, numbers))
    print(start, stop)
    return {chr(i): i for i in range(start, stop + 1)}


def show_dict(dict_):
    for items, value in dict_.items():
        print(f'{items} = {value}')


def check_numbers(numb):
    try:
        list(map(int, numb))
        logger_text = f'{numb = }; {type(numb)}'
        logger.info(logger_text)
    except ValueError as e:
        logger.error(e)


if __name__ == '__main__':

    FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
             '\nв строке {lineno:03d} функция "{funcName}()" ' \
             '\nв {created} секунд записала сообщение: {msg}\n\n'

    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='task_1.txt', filemode='a', encoding='utf-8', level=logging.INFO, format=FORMAT,
                        style='{')

    numbers = argv[1:]
    print(numbers)
    check_numbers(numbers)
    show_dict(create_dict_for_chr_ord())
