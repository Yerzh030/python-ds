# TODO здесь писать код
name = input("What is your name?")
while True:
    print("Input 1 to see chat text or 2  to write a message")
    response = input("Your input:")
    if response == "1":
        try:
            with open("chat.txt","r+") as file:
                message  = file.readlines()
                print(" ".join(message))
        except FileNotFoundError:
            print("File is not exitst")
    elif response == '2':
        new_message = input("input the message:")
        with open("chat.txt",'a') as file:
            file.write('{name}: {message}'.format(name = name, message= new_message))

