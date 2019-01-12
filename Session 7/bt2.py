while True:
    b = ["blue", "red", "teal", "green"]
    a = int(input("enter position:"))
    if 0 <= a <= len(b):
        print (b[a])
        break
    else:
        print("nhập lại:")