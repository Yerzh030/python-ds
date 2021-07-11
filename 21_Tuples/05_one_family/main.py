# TODO здесь писать код
family = { "Сидоров Никита": 35,
           "Сидорова Алина":34,
           "Сидоров Павел":10,
           "Климов Егор": 35,
           "Шашкина Алина":34,
           "Марков Павел":10
}
find_fm = input("Введите фамилию:").lower()
for key,value in family.items():
    if find_fm  in key.lower():
        print(key,value)
