# TODO здесь писать код
word = input("Введите слово:")
word = list(word)
count = 0
res =0
for symbol in word:
    for  comp in word:
        if symbol == comp:
            count +=1
    if count == 1:
        res +=1
    count = 0
print('Кол-во уникальных букв:',res)