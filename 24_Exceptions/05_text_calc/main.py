# TODO здесь писать код
sum =0
with open("calc.txt",'r+') as calc_file:
    for line in calc_file:
        try:
            num1,operation,num2 = line.split()
            num1 = int(num1)
            num2 = int(num2)
            if operation == '/':
                res = num1 / num2
                sum += res
                print(num1, operation, num2, " = ", res)
            elif operation == '+':
                res = num1 + num2
                sum += res
                print(num1,operation,num2," = ",res)
            elif operation == '*':
                res = num1 * num2
                sum += res
                print(num1,operation,num2," = ",res)
            elif operation == '-':
                res = num1 - num2
                sum += res
                print(num1,operation,num2," = ",res)
            else:
                raise BaseException("Неизвестная операция")
        except ValueError:
            print("Нельзя совершать мат операций с символами")
        else:
            print(sum)
