def code_pairs(num):
    list_check = []
    for i in range(3, num):
        if num % i == 0:
            for t in range(1, i):
                if t != (i - t):
                    lis = []
                    pairNumOne = t
                    pairNumTwo = (i - t)
                    for j in range(1):
                        lis.append(pairNumOne)
                        lis.append(pairNumTwo)
                    list_check.append(lis)

    for e in range(1, num):
        if e != (num - e):
            lis = []
            pairNumOne = e
            pairNumTwo = (num - e)
            for j in range(1):
                lis.append(pairNumOne)
                lis.append(pairNumTwo)
                list_check.append(lis)
    return list_check


def sorting_by_uniqueness(lis_proverki):
    result = []
    for h in range(len(lis_proverki)):
        list_ = []
        list_.extend(lis_proverki[h])
        revers_lis_proverki = list_[::-1]
        if revers_lis_proverki not in result:
            result.append(lis_proverki[h])
    return result


def cod(numbers):
    result = sorted(sorting_by_uniqueness(code_pairs(numbers)))
    str_result = ""
    for i in result:
        for j in i:
            str_result = str_result + str(j)
    print(str_result)


number = int(input("Введите число  от 3 до 20: "))
cod(number)
