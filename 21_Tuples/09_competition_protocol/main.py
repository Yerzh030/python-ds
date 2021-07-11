# TODO здесь писать код
n = int(input("Сколько записей заносится в протокол? "))
print("Записи (результат и имя:")
results = dict()
for i in range(n):
    record = input("{} запись:".format(i+1)).split()
    score = int(record[0])
    name = record[1]
    if name in results and results[name] < score:
        results[name] = score
    elif not name in results:
        results[name] = score
results = list(sorted(results.items(), key=lambda item: item[1],reverse=True)[:3])
for i,value in enumerate(results):
    n,sc = value
    print("{} место. {}  ({})".format(i+1,n,sc))