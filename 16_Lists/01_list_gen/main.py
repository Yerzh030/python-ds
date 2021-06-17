# TODO здесь писать код
def create_list(N):
    list = []
    for i in range(1,N+1):
        if i % 2 != 0:
            list.append(i)
    return  list

N = int(input("Введите N:"))
print(create_list(N))
