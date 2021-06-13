# TODO здесь писать код
def check_year(year):
    numone = numtwo = year
    count= 0
    while numone != 0:
        n1 = numone % 10
        count  = 1
        numone = numone // 10
        numtwo = numone
        while numtwo != 0:
            n2 = numtwo %10
            numtwo = numtwo //10
            if n1 == n2:
                count +=1
            if count == 3:
                return  True
    return  False

first_year = int(input("Введите первый год:"))
second_year = int(input("Введите второй год:"))
for i in range(first_year,second_year+1):
    if check_year(i) == True:
        print(i)
