# TODO здесь писать код
def sort_tuple(tup):
    nums = True
    for i, val in enumerate(tup):
        if not isinstance(val,int):
            nums = False
            break
    if nums:
         return sorted(tup)
    else:
        return  tup
tup = (1,33,12,12,11)
print(sort_tuple(tup))


