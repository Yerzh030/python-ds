# TODO здесь писать код
import os
numbers_file = open('numbers.txt','r')
sum = 0
for i_elem in numbers_file:
    i_elem = i_elem.strip()
    if i_elem.isnumeric():
        sum += int(i_elem)
sum_file = open("answer.txt",'w')
sum_file.write(str(sum))
