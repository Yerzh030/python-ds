# TODO здесь писать код
dictionary = dict()
while True:
    action = int(input("Выберите действие(1-добавить контакт,2 - поиск контакта):"))
    if action == 1:
        name = input("Введите имя:")
        surname = input("Введите фамилию:")
        phone = input("Номер телефона:")
        dictionary[(name,surname)] = phone
        print(dictionary)
    elif action == 2:
        surname = input("Введите фамилию:").lower()
        for key,value in dictionary.items():
           name,surn = key
           if surname == surn.lower():
               print(surn,value)
