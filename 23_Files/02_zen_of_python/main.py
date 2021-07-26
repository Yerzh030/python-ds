# TODO здесь писать код
import os
print(os.path.abspath("zen.txt"))
zen = open("zen.txt",'r')
prog = []
for i_elem in zen:
    prog.append(i_elem.strip())
for i in range(len(prog)-1,0,-1):
    print(prog[i])