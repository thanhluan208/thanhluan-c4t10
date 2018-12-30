while True:
    a = input("your password?")
    check = 0
    for i in a:
        if i.isdigit:
            check = 1
    if check == 0:
        print("vuilongnhaplai")
    elif check == 1:
        b = a.count("")
        if b > 8:
            print("vuilongnhaplai")
        else:
            if a == a.lower():
                print("vuilongnhaplai")
            elif a == a.upper():
                print("vuilongnhaplai")
            else:
                print(a)
                break
