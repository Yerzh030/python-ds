# TODO здесь писать код
arr = [0,0,0,11,122,33,0,0,12,0]
for i  in range(len(arr)):
     if arr[i] == 0:
         arr.pop(i)
         arr.append(0)
arr = [ arr[i] for i in range(len(arr)) if arr[i] != 0]
print(arr)