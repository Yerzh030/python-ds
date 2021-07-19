def calculating_math_func(data = 10):
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    return result

# TODO оптимизировать функцию
print(calculating_math_func())