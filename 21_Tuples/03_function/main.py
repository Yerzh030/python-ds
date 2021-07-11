# TODO здесь писать код
def change_tuple(tup,n):
    fp =0
    sp = 0
    for i, num in enumerate(tup):
        if  num == n and fp == 0:
            fp = i
        elif num == n and fp !=0:
            sp = i
    if sp == 0 and fp == 0:
        return ()
    else:
        if sp!=0:
            return  tup[fp:sp+1]
        else:
            return tup[fp::]
a = (1,5,3,1,5,1,61,1)
n = int(input())
print(change_tuple(a,n))
