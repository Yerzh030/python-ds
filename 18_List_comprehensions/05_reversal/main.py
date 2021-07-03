# TODO здесь писать код
text = input("Введите текст:")
arr = [ i for i in range(len(text)) if text[i] == 'h']
l = int(arr[0])
r = int(arr[1]) - 1
print(text[r:l:-1])