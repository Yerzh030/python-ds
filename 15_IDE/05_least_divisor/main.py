# TODO здесь писать код
def nd(n):
    min = n
    for i in range(2,n+1):
        if n % i == 0 and i < min:
            min = i
    return  min
n  = int(input("Введите число:"))
print("Наименьший делитель, отличный от единицы:",nd(n))