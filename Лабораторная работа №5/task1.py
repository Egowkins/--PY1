from pprint import pprint
# TODO решить с помощью list comprehension и распечатать его
num_of_dig = 16
bit_list = []
for i in range(num_of_dig):

    bit_dic = {'bin': bin(i), 'dec' : i, 'hex': hex(i), 'oct': oct(i)}
    bit_list += [bit_dic for _ in range(1)]

pprint(bit_list)
