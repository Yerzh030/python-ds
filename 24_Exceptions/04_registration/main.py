# TODO здесь писать код
def check_field(line):
    fields = line.split()
    if len(fields) < 3:
        return IndexError("Не присутствуют все три поля:")
    elif fields[0].isalpha() !=True:
        return NameError("поле имени содержит НЕ только буквы")
    elif "@" not in fields[1] or "." not in fields[1]:
        return SyntaxError("поле емейл НЕ содержит @ и .")
    elif int(fields[2]) < 10 or int(fields[2]) > 99 :
       return  SyntaxError("поле емейл НЕ содержит @ и .")
with open("registrations.txt",'r',encoding='utf-8') as register_file:
    for line in register_file:
        if check_field(line) is None:
            with open("registrations_good.log",'a') as good_log:
                good_log.write(line + '\n')
        else:
            with open("registrations_bad.log",'a') as bad_log:
                bad_log.write(line + " " +str(check_field(line)) + '\n')
