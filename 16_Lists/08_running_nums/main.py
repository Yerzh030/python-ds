# TODO здесь писать код
k = int(input("Сдвиг:"))
n = int(input("Кол- во элементов в списке: "))
list1 = []
for i in range(n):
    num = int(input())
    list1.append(num)
print("Изначальный список:",list1)
for i in range(k):
    list1.insert(0, list1.pop())
print("Сдвинутый список: ",list1)
