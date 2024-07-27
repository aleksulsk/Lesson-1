my_dict = {"Ivan": 1987, "Vasya": 2002, "Kolya":1999}
print(my_dict)
print(my_dict.get("Ivan"))
print(my_dict.get("Alex"))
my_dict.update({"Zhenya": 1985, "Kostya": 2005})
print(my_dict)
a = my_dict.pop("Ivan")
print(a)
print(my_dict)

my_set = {1, 2, 1, 2, "Hello", True, "Hello"}
print(my_set)
my_set.add(3)
my_set.add(4)
my_set.discard(2)
print(my_set)
