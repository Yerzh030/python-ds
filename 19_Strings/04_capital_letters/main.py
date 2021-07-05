# TODO здесь писать код
# TODO здесь писать код
def capital(text):
    res = ""
    for word in text:
        res +=" "+ word.capitalize()
    print(res)
row = input("Строка:").split()
capital(row)