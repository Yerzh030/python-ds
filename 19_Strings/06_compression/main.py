# TODO здесь писать код
word = input("Enter the word:")
count = 1
for  i in range(len(word)):
   if i !=(len(word) -1):
        if word[i] == word[i+1]:
            count +=1
        else:
            print(word[i] + str(count), end="")
            count = 1
   else:
       if word[i] != word[i-1]:
            print(word[i] + str(count),end='')
