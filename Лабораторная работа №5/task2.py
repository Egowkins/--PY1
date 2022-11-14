from random import sample


def get_unique_list_numbers(lmin: int = -10, rmax: int = 10,
                            lof_string: int = 15) -> list[int]:

    rand_list = [x for x in range(lmin, rmax, 1)]

    return sample(rand_list, lof_string)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
