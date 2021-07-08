# TODO здесь писать код
orders_count = int(input("Введите кол-во заказов: "))
orders = dict()
for i in range(orders_count):
    print("{} заказ:".format(i+1),end= ' ')
    order = input().split()
    name = order[0]
    pizza = order[1]
    count = int(order[2])
    if name in orders:
        if pizza in orders[name]:
            orders[name][pizza] +=count
        else:
            orders[name][pizza] = count
    else:
        orders[name] = {pizza:count}
for name in orders:
    print(name)
    for pizza in orders[name]:
        print("          ",pizza,orders[name].get(pizza))