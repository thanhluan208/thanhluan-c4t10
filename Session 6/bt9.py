a = ["Sport", "LOL", "DOTA", "BTS"]
while True:
    i = int(input("nhap vao 1 so : "))
    if 0 < i < len(a):
        a.pop(i)
        print(a)
        break
    else:
        print("nhập lại")