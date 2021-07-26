# TODO здесь писать код
import  os
re = open('first_tour.txt','r')
text = []
for line in re:
    text.append(line.strip().split())
qualify = text[0][0]
qualified = dict()
for i in range(1,len(text)):
    if int(text[i][2]) >= int(qualify):
        qualified[str(text[i][1])[0] + ". " + str(text[i][0])] = str(text[i][2])
re.close()
print(qualified)
second_tour = open("second_tour.txt","a+")
for key,value in qualified.items():
    second_tour.write(key + " " + value)
