# TODO здесь писать код
n = int(input("Кол-во человек:"))
lose = int(input("Какое число в считалке?"))
circle = list(range(1,n+1))
start = 0
while circle.__len__() != 0:
    print("Текущий круг людей:", circle)
    print("Начала счета с номера",circle[start])
    delete = (start +lose - 1) % len(circle)
    if circle[delete] == circle[-1]:
        start = 0
    else:
        start = delete
    print("Выбывает человек под номером",circle.pop(delete))
print("Остался человек под номером",circle[0])


