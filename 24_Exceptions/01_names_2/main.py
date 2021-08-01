# TODO здесь писать код
line_count =0
sym_sum = 0
with open("people.txt",'r') as people_file:
    for i_line in people_file:
        try:
            line_count +=1
            length = len(i_line)
            if i_line.endswith('\n'):
                length -=1
            if length < 3:
                raise BaseException
            sym_sum += length
        except BaseException:
            print("Длина {} строки меньше 3 символов".format(line_count))
print("Сумма символов:",sym_sum)
