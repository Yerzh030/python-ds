films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

# TODO здесь писать код
print("Какие у Вас любимые фильмы?")
favourite_movies = []
film = "!"
while film != "":
    film =input()
    if film in films:
        favourite_movies.append(film)
    else:
        print("Ошибка")
print(favourite_movies)
