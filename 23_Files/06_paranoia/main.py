# TODO здесь писать код
def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
import  os
file = open("text.txt","w+")
for _ in range(4):
    file.write("Hello \n")
file.close()
re = open('text.txt','r')
text = []
for line in re:
    text.append(line.strip())
cypher = open("cipher_text.txt",'a')
for i,el in enumerate(text):
    cypher.write(encrypt(el,i+1))
    cypher.write('\n')
cypher.close()