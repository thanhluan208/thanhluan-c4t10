
while True:
    a = int(input("nhập vào 1 số:"))
    if a <=0:
        print("vui lòng nhập lại")
    else:
        for a in range(a, 0, -1):
            print(a)
        break