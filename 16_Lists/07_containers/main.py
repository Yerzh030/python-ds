# TODO здесь писать код
n = int(input("Кол-во контейнеров:"))
blocks = []
for i in range(n):
    block = int(input("Введите вес контейнера:"))
    if block <= 200:
        blocks.append(block)
    else:
        print("Масса не должна превышвть 200")
new_block = int(input("Введите вес нового контейнера:"))
num =1
for i in range(n):
    if new_block <= blocks[i]:
        num += 1
print("Номер, куда встанет новый контейнер:", num)