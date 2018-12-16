while True:
    aabc = input("Enter a number:")
    check = 0
    for b in aabc:
        if b.isdigit:
            check = 1
    if check == 0:
        print("nhập lại")
    elif check == 1:
        c = aabc.count("") - 1
        print(c)
        break