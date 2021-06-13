# TODO здесь писать код
def count_sum(N):
    digit = 1
    sum =0
    while N >0:
        digit = N %10
        sum = sum +digit
        N = N//10
    return  sum
def count_digit(N):
    count =0
    while N >0:
        count = count +1
        N = N//10
    return count
N = int(input("Введите N:"))
sum = count_sum(N)
count = count_digit(N)
print("Сумма цифр:",sum)
print("Кол-во цифр:",count)
print("Разность суммы и кол-ва цифр",abs(count- sum))