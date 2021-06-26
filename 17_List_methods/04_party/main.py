guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
print("Сейчас на вечериинке",guests.__len__(),"человек:",guests)
guest = input("Гость пришел или ушел?")
while guest != "Пора спать":
    name = input("Имя гостя:")
    if guests.__len__() == 6 and guest == 'пришел':
        print("Прости,",name,"но мест нет.")
    elif guests.__len__() < 6 and guest == 'пришел':
        print("Привет,", name, "!")
        guests.append(name)
    else:
        print("Пока,",name,"!")
        guests.remove(name)
    print("Сейчас на вечериинке", guests.__len__(), "человек:", guests)
    guest = input("Гость пришел или ушел?")
print("Вечеринка закончилась, все легли спать.")
