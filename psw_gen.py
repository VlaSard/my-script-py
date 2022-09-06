"""Генератор паролей с настройкой и выбором:
 - записать список паролей в файл или
 - вывести список в консоль.
"""
import random
from string import ascii_lowercase, ascii_uppercase, digits

# Первоначальное значение, для запуска программы.
ANSWER = True


def get_pools(message: str, default: bool) -> bool:
    """Функция обработки ответа пользователя на запросы программы.
    Возвращаемое значение по умолчанию передается в переменной default.
    В переменной message передаем сообщение с вопросом.

    При не допустимом ответе на запрос:
    выводится сообщение с допустимыми вариантами ответа.

    Возвращаем True или False.
    """
    yes_pools = ['д', 'да', 'y', 'yes']
    no_pools = ['н', 'нет', 'n', 'no']
    yes_or_no = '(д/н или да/нет: ' + \
                ('да' if default else 'нет') + \
                ' - по умолчанию): '
    while True:
        flag = input(f'{message} {yes_or_no}').strip().lower()
        if len(flag) == 0:
            return default
        if flag in yes_pools:
            return True
        if flag in no_pools:
            return False
        print(f"Требуется ввести {yes_or_no}. Повторите попытку.")


def get_chars() -> list:
    """
    Функция настройки списка символов.
    Задает какие символы будут использоваться в пароле.
    """
    punctuation = '!#$%&*+-=?@^_'
    chars = []
    if get_pools('В пароле использовать цифры?', True):
        chars.extend(digits)
    if get_pools('В пароле использовать буквенные символы нижнего регистра?',
                 True):
        chars.extend(ascii_lowercase)
    if get_pools('В пароле использовать буквенные символы верхнего регистра?',
                 True):
        chars.extend(ascii_uppercase)
    if get_pools('В пароле использовать знаки пунктуации?', False):
        chars.extend(punctuation)
    random.shuffle(chars)
    if get_pools('Исключать неоднозначные символы il1LoO0?', False):
        for char in 'il1LoO0':
            chars.remove(char)
    return chars


def get_answer(messages: str) -> int:
    """Функция запроса длинны и количества паролей."""
    while True:
        answer_in = input(f'{messages}: ')
        if not answer_in.isdigit():
            print('Допустимое значение - числовое. Попробуйте еще раз.')
        else:
            return int(answer_in)


def get_output_pas(password: tuple[str]):
    """Функция записывает в файл или выводит в консоль список паролей."""
    if get_pools('Сохранить пароли в файл?', True):
        with open('password.txt', 'w', encoding='utf-8') as file_pass:
            file_pass.writelines('Список паролей:\n\n')
            for psw in password:
                file_pass.writelines(f'{psw}\n')
    else:
        print('Список паролей:')
        for psw in pass_list:
            print(psw)


while ANSWER:
    LENGTH = get_answer('Введите длину генерируемого пароля')
    AMOUNT = get_answer('Введите количество необходимых паролей')

    # Создаем список символов для генерации пароля.
    CHARS = get_chars()

    # Создаем список паролей.
    pass_list = tuple((''.join([random.choice(CHARS)
                                for _ in range(LENGTH)]))
                      for _ in range(AMOUNT)
                      )

    # Записываем в файл или выводим в консоль список паролей.
    get_output_pas(pass_list)

    # Запрос на создание еще одного списка.
    ANSWER = get_pools('Продолжить?', False)
