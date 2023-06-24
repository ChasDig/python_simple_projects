import random
import math

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
NUMBER = "0123456789"
SPECIAL = "@#$%&*"

length = int(input("Enter length password: "))


def generate_password(len_password, array, is_alphabet=False):
    password = []
    for item in range(len_password):
        index = random.randint(0, len_password - 1)
        meaning = array[index]
        if is_alphabet:
            register = random.randint(0, 1)
            if bool(register):
                meaning = meaning.upper()
        password.append(meaning)
    return password


def join_password(result_gen_alphabet, result_gen_number, result_gen_special):
    list_password = result_gen_alphabet + result_gen_number + result_gen_special
    return "".join(list_password)


def create_password(len_password):

    # 50/30/20
    alphabet_len = length // 2
    number_len = math.ceil(length / 100 * 30)
    special_len = length - (alphabet_len + number_len)

    result_gen_alphabet = generate_password(
        len_password=alphabet_len,
        array=ALPHABET,
        is_alphabet=True,
    )
    result_gen_number = generate_password(
        len_password=number_len,
        array=NUMBER,
        is_alphabet=False,
    )
    result_gen_special = generate_password(
        len_password=special_len,
        array=SPECIAL,
        is_alphabet=False,
    )
    new_password = join_password(result_gen_alphabet, result_gen_number, result_gen_special)
    return new_password


if __name__ == "__main__":
    password_result = create_password(len_password=length)
    print(password_result)
