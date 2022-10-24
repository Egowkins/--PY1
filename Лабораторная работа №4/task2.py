def get_count_char1(str_):
    # TODO вернуть словарь где частота символа заменена на процентное соотношение ко всем остальным
    dictnr = get_count_char(str_)
    count = 0
    for char in dictnr:
        count += dictnr.get(char)
    for char in dictnr:
        dictnr[char] = round(dictnr[char] / count * 100, 3)
    return dictnr


def get_count_char(str_):
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = str_.lower()
    str_ = str_.split()
    str_ = "".join(str_)
    chars = {}

    for char in str_:
        if char.isalpha() is True and char in chars:
            chars[char] += 1
        elif char.isalpha() is True:
            chars[char] = 1
    return chars


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
#print(get_count_char1(main_str))
