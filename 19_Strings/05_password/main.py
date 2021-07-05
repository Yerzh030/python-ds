# TODO здесь писать код
while True:
    password = input("Enter the password:")
    if len(password) < 8 or password.lower() == password or sum([1 for char in password if char.isdigit()]) < 3:
        print("Password is not secure. Try again")
    else:
        print("Succes")
        break
