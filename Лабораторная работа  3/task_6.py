list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
maxel = 0
low = list_numbers[len(list_numbers) - 1]
maxi = list_numbers[0]
for i in range(len(list_numbers)):

    current_maxi = list_numbers[i]
    if current_maxi > maxi:
        maxi = current_maxi
        maxel = i

list_numbers[len(list_numbers) - 1] = maxi
list_numbers[maxel] = low
print(list_numbers)
