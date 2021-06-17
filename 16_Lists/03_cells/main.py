# TODO здесь писать код
n = int(input("Кол-во клеток:"))
ch = []
for i in range(n):
    print("Эффективность", i+1, "клетки:", end="")
    num = int(input())
    if num < i:
        ch.append(num)
print("Не подходящие значения:",end=" ")
for i in range(len(ch)):
    print(ch[i],end=' ')

