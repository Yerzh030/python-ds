# TODO здесь писать код
n = int(input("Кол-во виеокарт:"))
videocard = []
max = 0
for i in range(n):
    print(i + 1, "Видеокарта: ", end='')
    element = int(input())
    videocard.append(element)
    if element > max:
        max = element
print("Старый список видеокарт: ", videocard)
videocard_new =[]
for i in range(n):
    if videocard[i] != max:
        videocard_new.append(videocard[i])
print("Новый список видеокарт:", videocard_new)
