import random
import sys

TEXT_WITH_RULES = """Игра Бейглс:
Правила игры:
    - игроку дается ограниченное число попыток, за которые он должен угадать правильную последовательность чисел;
    - если игрок ввел правильную цифу, но не на правильном месте, выведется 'Правильная цифра';
    - если игрок ввел правильную цифру и верное ее расположение, то выведется 'Правильное место';
    - если игрок не угадал ни последовательность чисел, ни местоположение хотя бы одной из цифр или ее значение, то
    выведется 'Ничего не угадал';
    - если игрок угадал все цифры и их правильное расположение(последовательность), выведется 'Угадал' и игра окончится;
    - для выхода из игры следует ввести 'exit'.
"""
RANGE = 10
SECRET_SYMBOLS = [str(number) for number in range(RANGE)]
print(TEXT_WITH_RULES)


def check_exit(input_user: str):
    if input_user == "exit":
        print("Спасибо за игру!")
        sys.exit()


def check_integer_isinstance(input_user: str):
    try:
        int(input_user)
        return True
    except ValueError as _:
        print("Ошибка при вводе данных, повторите попытку ввода значений или введите 'exit' для выхода.")
    return False


def check_secret_character_length(secret_character_length: str) -> int:
    secret_character_length = int(secret_character_length)
    while True:
        if (secret_character_length > 6) or (secret_character_length < 3):
            secret_character_length = int(input("Введите количество цифр в искомом числе (мин. - 3, макс. - 6): "))
        else:
            break
    return secret_character_length


def check_number_of_attempts(number_of_attempts: str) -> int:
    number_of_attempts = int(number_of_attempts)
    while True:
        if (number_of_attempts > 20) or (number_of_attempts < 1):
            number_of_attempts = int(input("Введите количество попыток (минимум - 1, максимум 20): "))
        else:
            break
    return number_of_attempts


def input_user_data():
    check_int_number_of_attempts, check_int_secret_character_length = False, False
    number_of_attempts, secret_character_length = "", ""
    while not check_int_number_of_attempts and not check_int_secret_character_length:
        number_of_attempts = input("Введите количество попыток (минимум - 1, максимум 20): ")
        check_exit(number_of_attempts)
        check_int_number_of_attempts = check_integer_isinstance(number_of_attempts)
        secret_character_length = input("Введите количество цифр в искомом числе (минимум - 3, максимум - 6): ")
        check_exit(secret_character_length)
        check_int_secret_character_length = check_integer_isinstance(secret_character_length)
    return number_of_attempts, secret_character_length


def create_secret_number(len_secret_number: int) -> list:
    random.shuffle(SECRET_SYMBOLS)
    list_secret_number = []
    for item in range(len_secret_number):
        list_secret_number.append(SECRET_SYMBOLS[item])
    return list_secret_number


def check_secret_number(input_number: str, secret_number: list):
    result = []
    for item in range(len(secret_number)):
        if input_number[item] == secret_number[item]:
            result.append("Правильное место")
        elif input_number[item] in secret_number:
            result.append("Правильная цифра")
    if result == ["Правильное место", "Правильное место", "Правильное место"]:
        result = "Угадал"
    if not result:
        result.append("Ничего не угадал")
    if isinstance(result, list):
        random.shuffle(result)
    return result


def start_game():
    number_of_attempts, secret_character_length = input_user_data()
    len_secret_number = check_secret_character_length(secret_character_length)
    number_of_attempts = check_number_of_attempts(number_of_attempts)
    secret_number = create_secret_number(len_secret_number=len_secret_number)
    print("[!] Секретное число: ", secret_number)
    result_check = ""
    attempt = 1
    while result_check != "Угадал":
        input_number = input(f"Попытка #{attempt}. Введите число: ")
        check_exit(input_user=input_number)
        check_integer_isinstance(input_user=input_number)
        if len(input_number) != len(secret_number):
            print(f"Длина вашего номера не равна длине загаданного числа. "
                  f"Длина загаданного числа - {len(secret_number)}")
        else:
            result_check = check_secret_number(input_number, secret_number)
            print("Результат: ", result_check)
            attempt += 1
            if attempt - 1 == int(number_of_attempts):
                print(f"Количество попыток закончено! Загаданное число - {secret_number}")
                return "BadEndaGame"
    join_secret_number = "".join(secret_number)
    print(f"Поздравляю, Вы выйграли!\nПотрачено попыток: {attempt}.\nЗагаданное число: {join_secret_number}.")
    return "GoodEndGame"


if __name__ == "__main__":
    start_game()
