# TODO здесь писать код
N = int(input("Кол-во друзей:"))
K = int(input("Долговых расписок:"))
balance = []
for i in range(N):
    balance.append(0)
for i in range(K):
    print(i+1,"Расписка")
    to = int(input("Кому:"))
    fr = int(input("От кого:"))
    money = int(input("Сколько:"))
    balance[to-1] += money
    balance[fr-1] -= money
count = 1
for i in balance:
    print(count,":",i)
    count +=1
