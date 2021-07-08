# TODO здесь писать код
import random

N = int(input("Введите максимальное число:"))
wish = random.randint(1,N)
while  True:
    numbers  = input("Нужное число есть среди вот этих чисел: ")
    if numbers != 'Помогите!':
        numbers = set( int(n) for  n in numbers.split())
        if wish in numbers:
            print("да")
        else:
            print("Нет")
    else:
        num = {i for i in range(wish,wish - 6, -2)}
        print("Артём мог загадать следующие числа:",num)
        break
