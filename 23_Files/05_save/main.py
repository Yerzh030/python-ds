# TODO здесь писать код
import os
def find_dir(dir,path):
    if dir in os.listdir(path):
        return os.path.join(path,dir)
    else:
        os.mkdir(os.path.join(path, dir))
        return os.path.join(path, dir)
text = input("Введите строку: ")
print("Куда хотите сохранить документ? Введите последовательность папок (через пробел):")
path = input().split()
name = input("Введите имя файла: ")
st = "C://"
for i,el in enumerate(path):
    st = find_dir(el,st)
completeName = os.path.join(st, name+".txt")
file1 = open(completeName, "w")
file1.write(text)
file1.close()