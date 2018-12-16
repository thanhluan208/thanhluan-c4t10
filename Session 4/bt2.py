while True:
    a = input("your password?")
    check = 0
    for i in a:
        if i.isdigit:
            check = 1
    if check == 0:
        print("nhaplaipassword")
    elif check == 1:
        b = a.count("")
        if b > 8:
            print("nhaplaipassword")
        else:
            print(a)
            break