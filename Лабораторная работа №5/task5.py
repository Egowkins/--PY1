from random import sample
import string


def get_random_password(n=8) -> str:

    leta = string.ascii_uppercase
    let_a = string.ascii_lowercase
    num = string.digits
    all_symbols = sample(leta + let_a + num, n)

    return all_symbols


print(get_random_password())
