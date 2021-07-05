# TODO здесь писать код
def maxword(text):
    max =0
    index = 0
    for i in range(len(text)):
        if len(text[i]) > max:
            max = len(text[i])
            index = i
    print("Длина слова:",max)
    print("Слово:",text[index])
row = input("Строка:").split()
maxword(row)    