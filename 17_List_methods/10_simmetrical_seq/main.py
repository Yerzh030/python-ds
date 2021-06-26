# TODO здесь писать код
def is_polindrome(list1):
    reversed_list = []
    for i in range(len(list1) - 1, -1,-1):
        reversed_list.append(list1[i])
    if list1 == reversed_list:
        return True
    else:
        return  False
n = int(input("Кол-во чисел:"))
list1 = []
for i in range(n):
    n = int(input("Число:"))
    list1.append(n)
new_list = []
ans = []
for i in range(0,len(list1)):
    for j in range(i,len(list1)):
        new_list.append(list1[j])
    if is_polindrome(new_list):
        for i_ans in range(0,i):
            ans.append(list1[i_ans])
        ans.reverse()
        break
    new_list = []
print("Исходный список", list1)
print("Нужно чисел для палиндрома:", len(ans))
print("Числа:", ans)

