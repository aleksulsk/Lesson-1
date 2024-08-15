summa = 0


def chek_int(value):
    if not isinstance(value, int):
        for i in value:
            calculate_structure_sum(i)


def calculate_structure_sum(*values):
    global summa
    for value in values:
        if isinstance(value, int):
            summa = summa + value
            return summa

        elif isinstance(value, str):
            summa = summa + len(value)
            return summa

        elif isinstance(value, dict):
            pairs = list(value.items())
            chek_int(pairs)

        elif isinstance(value, tuple):
            if not isinstance(value, int):
                for i in value:
                    calculate_structure_sum(i)

        elif isinstance(value, list):
            chek_int(value)

        elif isinstance(value, set):
            chek_int(value)
    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)