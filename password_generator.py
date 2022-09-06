import random
from string import ascii_lowercase, ascii_uppercase, digits

answer = True


def get_pools(message, default):
    yes = ['д', 'да', 'y', 'yes']
    no = ['н', 'нет', 'n', 'no']
    yes_or_no = f'(д/н или да/нет: ' + ('да' if default else 'нет')\
                + ' - по умолчанию): '
    while True:
        flag = input(f'{message} {yes_or_no}').strip().lower()
        if len(flag) == 0:
            return default
        if flag in yes:
            return True
        if flag in no:
            return False
        print(f"Требуется ввести {yes_or_no}. Повторите попытку.")


def get_password(len_pas, chars):
    return ''.join([random.choice(chars) for _ in range(len_pas)])


def get_password_list(number):
    psw_list = list()
    for i in range(number):
        psw_list.append(get_password(length, char_list))
    return psw_list


def get_chars():
    punctuation = '!#$%&*+-=?@^_'
    chars = list()
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


def get_answer(messages):
    while True:
        answer_in = input(f'{messages}: ')
        if not answer_in.isdigit():
            print(f'Допустимое значение - числовое. Попробуйте еще раз.')
        else:
            return int(answer_in)


while answer:
    length = int(get_answer('Введите длину генерируемого пароля'))
    amount = int(get_answer('Введите количество необходимых паролей'))
    char_list = get_chars()

    pass_list = get_password_list(amount)
    print(f'Список паролей:\n', *pass_list)
    answer = get_pools('Продолжить?', False)
