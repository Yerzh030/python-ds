# TODO здесь писать код
def is_prime(n):
    result  = True
    for i in range(2,n//2+1):
        if n % i == 0:
            result = False
            break
    return  result

def prime_items(iterable):
    return  [ v for i, v in enumerate(iterable) if is_prime(i) and i!=0 and i!=1]
a = (1,3,31323,32,32,32)
print(prime_items(a))