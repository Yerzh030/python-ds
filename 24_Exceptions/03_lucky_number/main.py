# TODO здесь писать код
import random
sum = 0

try:
    with open("result.txt", 'a') as result_file:
        while True:
            n = int(input("Введите число:"))
            sum = sum + n
            print(sum)
            if sum >=777:
                break
            random_exception = random.randint(1,13)
            if random_exception == 13:
                raise BaseException("Случайная ошибка")
                break
            result_file.write(str(n) + '\n')
except OverflowError:
    print("результат арифметической операции слишком велик для представления")