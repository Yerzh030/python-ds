# TODO здесь писать код
def shift(row,step):
    for i in range(step):
        row.insert(0, row.pop())
    return  row
word1 = list(input("First row:"))
word2 = input("Second row:")
for i in range(len(word1)):
    list1 = list(word2)
    shift(list1,i)
    if "".join(word1) == "".join(list1):
        print("Первая строка получается из второй со сдвигом")
