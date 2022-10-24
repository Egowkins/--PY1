import random


def get_unique_list_numbers() -> list[int]:

    rand_list = [x for x in range(-10, 10)]
    random.shuffle(rand_list)

    return rand_list[:15]


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
