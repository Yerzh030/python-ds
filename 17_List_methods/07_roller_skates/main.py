# TODO здесь писать код
skates = []
sizes = []
n = int(input("Кол-во коньков:"))
for i in range(n):
   print("Размер ", i+1 , "пары:",end = ' ')
   skate = int(input())
   skates.append(skate)
print()
k =int(input("Кол-во людей:"))
for i in range(k):
   print("Размер ноги ", i+1 , "человека:",end = ' ')
   size = int(input())
   sizes.append(size)
skates.sort()
sizes.sort()
count = 0
j = 0
i = 0
while  i < k:
    if sizes[i] == skates[j]:
        count +=1
        i = i + 1
        j = j + 1
    elif sizes[i] > skates[j]:
        j =  j + 1
    else:
        i = i + 1
print("Наибольшее кол-во людей могут взять коньки:",count)