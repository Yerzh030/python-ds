# TODO здесь писать код
messsage = input("Message:").split()
new_message =[word[-2::-1] + word[-1] if ( word.endswith(",") or word.endswith("?")
                                           or word.endswith(".") or word.endswith("!")) else word[::-1] for word in messsage ]
print("New message: "," ".join(new_message))
