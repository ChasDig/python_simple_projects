from collections import Counter
import sys
import datetime
import random

MIN_SIZE_ITER = 3
MAX_SIZE_ITER = 50
MIN_SIZE_BIRTHDAY = 10
MAX_SIZE_BIRTHDAY = 50
BASE_DATE = datetime.date(year=2000, month=1, day=1)

OUTPUT_TEXT = """Результаты генерирования:
- Количество стеков с генерациями: {};
- Количество генираций в каждом стеке: {};
- Ниже представлены результаты по каждому стеку с генерированием:
"""
OUTPUT_TEXT_STACK = "\t-- Попытка №{}, дата: {}, количество повторов данной даты - {}."


def check_exit(user_input: str) -> None:
    if user_input.lower() == "exit":
        sys.exit()


def check_size_number(number: int, max_size: int, min_size: int) -> bool:

    if min_size <= number <= max_size:
        return True
    raise ValueError


def input_data() -> tuple:
    while True:
        try:
            count_iter = input(
                f"Введите количество операций по генерированию дней рождения"
                f"(мин. - {MIN_SIZE_ITER}, макс. - {MAX_SIZE_ITER}). Для выхода, введите 'exit':\n>_ ",
            )
            check_exit(user_input=count_iter)
            int_count_iter = int(count_iter)
            check_size_number(
                number=int_count_iter,
                min_size=MIN_SIZE_ITER,
                max_size=MAX_SIZE_ITER,
            )
            count_birthday = input(
                "Введите количество дней рождений,генерируемых в одной опперации"
                f"(мин. - {MIN_SIZE_BIRTHDAY}, макс. - {MAX_SIZE_BIRTHDAY}). Для выхода, введите 'exit':\n>_ ",
            )
            check_exit(user_input=count_birthday)
            int_count_birthday = int(count_birthday)
            check_size_number(
                number=int_count_birthday,
                min_size=MIN_SIZE_BIRTHDAY,
                max_size=MAX_SIZE_BIRTHDAY,
            )
            break
        except ValueError as _:
            print("     Введено неверное значение. Повтрите попытку или введите 'exit' для выхода.")
    return int_count_iter, int_count_birthday


def birthday_match_check(list_birthday: list[list]) -> dict[int, dict[str, int]]:
    recurring_birthday = {}
    for item in range(len(list_birthday)):
        buffer_recurring_birthday = {}
        tuple_birthday = tuple(list_birthday[item])  # For hashing list_birthday
        count_birthday = Counter(tuple_birthday)
        for key, value in count_birthday.items():
            if value > 1:
                buffer_recurring_birthday[key] = value
        recurring_birthday[item] = buffer_recurring_birthday
    print(recurring_birthday)
    return recurring_birthday


def generate_list_random_birthday(count_birthday: int) -> list:
    list_random_birthday = []
    for item in range(count_birthday):
        random_date_delta = datetime.timedelta(random.randint(1, 365))
        list_random_birthday.append(BASE_DATE + random_date_delta)
    return list_random_birthday


def generate_iter_with_random_birthday(count_iter: int, count_birthday: int) -> list:
    dict_random_birthday = []
    for item in range(count_iter):
        dict_random_birthday.append(generate_list_random_birthday(count_birthday=count_birthday))
    return dict_random_birthday


def output_data(
        result_birthday_match_check: dict[int, dict[str, int]],
        count_iter: int,
        count_birthday: int,
) -> None:
    print(OUTPUT_TEXT.format(count_iter, count_birthday), end="")
    # print("Словарь с датами: ", result_birthday_match_check)
    buffer_check = 0
    for key_stack, data in result_birthday_match_check.items():
        for key_date, count in data.items():
            buffer_check += 1
            print(OUTPUT_TEXT_STACK.format(key_stack, key_date, count))
    if buffer_check == 0:
        print("\t-- Совпадения не были найдены.")


def main():
    count_iter, count_birthday = input_data()
    list_birthday = generate_iter_with_random_birthday(
        count_iter=count_iter,
        count_birthday=count_birthday,
    )
    result_birthday_match_check = birthday_match_check(list_birthday)
    return result_birthday_match_check, count_iter, count_birthday


if __name__ == "__main__":
    output_data(*main())
