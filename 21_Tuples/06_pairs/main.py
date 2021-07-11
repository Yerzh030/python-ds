# TODO здесь писать код
a =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a1 = [val for i,val in enumerate(a) if i % 2 == 0]
a2 = [val for i,val in enumerate(a) if i % 2 != 0]
a = list(zip(a1,a2))
print(a)
