
def separation_whole(number):
    number = str(number)
    flag = True
    whole = ""
    fraction = ""
    for symbol in number:
        if symbol == '.':
            flag = False
        elif flag:
            whole = whole + symbol
        else:
            fraction = fraction + symbol
    whole = reverse(int(whole))
    fraction = reverse(int(fraction))
    res = whole + "." + fraction
    return float(res)
def reverse(N):
  N = int(N)
  dec = ""
  while N != 0:
     dig = N % 10
     dec +=str(dig)
     N = N //10
  return  dec
N = float(input("Введите первое число:"))
K = float(input("Введите второое число:"))
print()
N = separation_whole(N)
K = separation_whole(K)
print("Первое число наоборот: ",N)
print("Второе число наоборот: ",K)
print()
print("Сумма: ", N+K)
