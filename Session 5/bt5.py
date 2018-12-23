
while True:
    a = int(input("nhập vào 1 sô:"))
    if a <= 0:
        print("nhập lại:")
    else:
        for a in range(1, a):
            print(a)
        break