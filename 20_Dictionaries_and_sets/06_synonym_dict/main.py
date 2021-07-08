# TODO здесь писать код
n = int(input("Введите количество пар слов:"))
dictionary = dict()
for i in range(n):
    print("{} пара: ".format(i+1),end=' ')
    syn = input().split(" - ")
    dictionary[syn[0].lower()] = syn[1].lower()
    dictionary[syn[1].lower()] = syn[0].lower()
while True:
    word = input("Введите слово: ").lower()
    if dictionary.get(word) is not None:
        print("Синоним: ",dictionary.get(word))
        break
    else:
        print("Такого слова в словаре нет.")