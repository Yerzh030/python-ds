# TODO здесь писать код
N = int(input("Кол-во палок:"))
k = int(input("Кол-во бросков:"))
sticks = ["|" for i in range(1,N+1)]
for i in range(k):
   l_i = int(input("Сбита с "))
   r_i = int(input("Сбита по "))
   r_i = r_i +1
   sticks[l_i:r_i] = ['.' for i in range(l_i,r_i)]
print(sticks[1:])