while True:
    password = input("your password?")
    check = 0
    for i in password:
        if i.isdigit():
            check = 1
    if check == 0:
        print("nhaplaipassword")
    elif check == 1:
        print(password)
        break


