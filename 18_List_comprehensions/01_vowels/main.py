# TODO здесь писать код
text = input("Введите текст:")
array = [ symbol for  symbol in text if symbol in "АУОЫИЭЯЮЁЕауоыиэяюёе"]
print('Cписок гласных букв:',array)
print("Длина списка:",len(array))