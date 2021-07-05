# TODO здесь писать код
ip = input("IP:").split(".")
res = 1
for num in ip:
    if num.__contains__(","):
        print("Адрес - это четыре числа, разделенные точками")
        res = 0
        break
    elif not num.isdigit():
        print(num,"is not digit")
        res = 0
        break
    elif  int(num) > 255:
        print(num, "is more than 255")
        res = 0
        break
    elif int(num) < 0:
        print(num, "is less than  0")
        res = 0
        break
if res == 1:
    print("IP-адрес корректен")