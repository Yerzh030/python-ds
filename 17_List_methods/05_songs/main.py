violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
# TODO здесь писать код
sum = 0
number_of_songs = int(input("Сколько песен надо выобрать?"))
for  i in range(number_of_songs):
    print("Название",i+1,"песни:",end = " ")
    name = input()
    for song in violator_songs:
        if name == song[0]:
            sum +=song[1]
print("Общее время:",round(sum,2), 'минут')

