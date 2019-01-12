while True:
    a = ["Sport", "LOL", "DOTA", "BTS"]
    b = input("nhập vào 1 giá trị : ")
    if b in a:
        a.remove(b)
        print(a)
        break
    else:
        print("nhập lại")