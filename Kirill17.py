def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 22)
print_params(c = [1, 2, 2])

list_ = [1, 2, 6]
print_params(*list_)

values_dict = {'a': 22, 'b': 1234, 'c': 421}
print_params(**values_dict)

values_list_2 = [1, 'Kirill']
print_params(*values_list_2, 24)
