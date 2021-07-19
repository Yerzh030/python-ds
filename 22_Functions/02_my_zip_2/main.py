# TODO здесь писать код
def short_seq(obj1 , obj2):
    return min(len(obj1),len(obj2))
pairs = []
def cus_zip(obj1,obj2):
    if short_seq(obj1,obj2) == 0:
        return tuple(pairs)
    else:
        pairs.append((obj1.pop(0),obj2.pop(0)))
        return cus_zip(obj1,obj2)
a = [1,2,3,4,5]
b = ['a','b','c']
print(cus_zip(a,b))
