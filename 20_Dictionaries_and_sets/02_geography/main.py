N = int(input("Кол-во стран: "))
countries = dict()
for i in range(N):
    print("{} страна:".format(i+1),end="")
    value  = input().split()
    countries[value[0]] = { value[i] for i in range(1,4)}
print(countries)
for i in range(3):
    print("{} город: ".format(i+1),end = " ")
    city = input()
    res = 0
    for country in countries:
        if city in countries[country]:
            print("Город {} распложен в стране {}".format(city,country))
            res = 1
    if res == 0:
        print("По городу {} данных нет.".format(city))
