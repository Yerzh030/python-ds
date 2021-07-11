def custom_zip(str,tup):
    res = []
    for i in range(len(tup)):
        res.append((str[i],tup[i]))
    res = tuple(res)
    print(res)
string  ="abcd"
tup =  (10, 20, 30, 40)
custom_zip(string,tup)
