a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lst = []#список простых чисел
lst1 = []#список непростых чисел
for i in range(2, 16):
    for j in range(2, i):
        if i % j == 0:
            lst1.append(i)
            # если делитель найден, число не простое.
            break
    else:
        lst.append(i)
print("Primes", lst)

print("Not_primes", lst1)

