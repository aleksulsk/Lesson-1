def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params()
print_params (2, 3, 3)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [11, "string", True]
values_dict = {"a": 1, "b": "string", "c": True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [123, "Number Two"]
print_params(*values_list_2, 42)