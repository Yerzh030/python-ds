# TODO здесь писать код
import os
file = "zen.txt"
path = os.path.abspath(os.path.join('../02_zen_of_python',file))
file = open(path,"r")
prog = []
for i_elem in file:
    prog.append(i_elem.strip())
letters= 0
words=0
row=len(prog)
for i,el in enumerate(prog):
    for letter in el:
        if letter in 'qwertyuiopasdfghjklmnbvcxz':
            letters +=1
    words += len(el.split())
print("Rows:{}, letters:{}, words:{}".format(row,letters,words))