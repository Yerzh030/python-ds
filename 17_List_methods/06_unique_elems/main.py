# TODO здесь писать код
list1 = []
list2 = []
for i in range(3):
    num = int(input("Введите число для первого списка:"))
    list1.append(num)
for i in range(7):
    num = int(input("Введите число для второго списка:"))
    list2.append(num)
print("Первый список:",list1)
print("Второй список:",list2)
list1.extend(list2)
unique_numbers = list(set(list1))
print(unique_numbers)

