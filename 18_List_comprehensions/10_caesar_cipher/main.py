# TODO здесь писать код
text =input("Ввеидте сообщение:")
shift = int(input("Сдвиг:"))
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
cypher = [ alphabet[(alphabet.index(sym)+shift) % 33] if sym != ' ' else ' ' for sym in text]
answer = ''
for sym in cypher:
    answer +=sym
print(answer)
