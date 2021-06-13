# TODO здесь писать код
import math
def check_r(x,y,r):
    h = math.sqrt(x**2 + y**2)
    if h > r:
        print('Монетки рядом нет')
    else:
        print("Монетка где-то рядом")
x = float(input("X:"))
y = float(input("Y:"))
r = float(input("r:"))
check_r(x,y,r)