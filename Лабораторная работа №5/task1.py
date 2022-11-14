from pprint import pprint
# TODO решить с помощью list comprehension и распечатать его
num_of_dig = 16
bit_list = []
bit_list = [{'bin': bin(i), 'dec' : i, 'hex': hex(i), 'oct': oct(i)} for i in range(num_of_dig)]
pprint(bit_list)

