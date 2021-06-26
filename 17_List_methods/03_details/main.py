shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

# TODO здесь писать код
detailc = input("Название детали:")
count = 0
sum = 0
for details in shop:
    if details.count(detailc) > 0:
        count += details.count(detailc)
        sum += details[1]
print("кол-во деталей:",count)
print("Общая стоимость:", sum)
