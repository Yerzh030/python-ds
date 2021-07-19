# TODO здесь писать код
def nums(n):
    print(n)
    if n > 1:
        return nums(n-1)
    else:
        return  1
num = int(input())
nums(num)