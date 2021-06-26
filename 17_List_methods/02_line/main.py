# TODO здесь писать код
class1 = []
class2 = []
class1.extend(range(160,177,2))
class2.extend(range(162,181,3))
class1.extend(class2)
class1.sort()
print(class1)