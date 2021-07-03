# TODO здесь писать код
import  random
N = 20
arr1 = [random.uniform(5,10) for i in range(N)]
arr2 = [random.uniform(5,10) for i in range(N)]
arr3 = [arr1[i]  if arr1[i] >= arr2[i] else arr2[i] for i in range(N)]
print("Первая команда:",arr1)
print("Вторая команда:",arr2)
print("Победители тура:",arr3)
