# TODO здесь писать код
def hs(text):
    symbols = dict()
    count =0
    for sym in text:
        if sym in symbols:
            symbols[sym] +=1
        else:
            symbols[sym] =1
    return symbols
def invert(dic):
    new_dic = dict()
    for i in dic.keys():
        if  dic[i] in new_dic:
            new_dic[dic[i]].append(i)
        else:
            new_dic[dic[i]] = [i]
    return  new_dic
text = input("Введите текст: ").lower()
symtable = hs(text)
print("Оригинальный словарь частот:")
for i in symtable.keys():
   print(i," : ",symtable[i])
syminvert = invert(symtable)
print("Инвентированный словарь частот:")
for i in syminvert.keys():
   print(i," : ",syminvert[i])