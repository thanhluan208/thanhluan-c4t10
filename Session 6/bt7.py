a = ["evenger1", "avenger2", "averger3"]
while True:
    i = int(input("nhap vao 1 so : "))
    m = input("nhap thay doi : ")
    if  0 < i < len(a):
        a [i] = m
        print(a)
        break
    else:
        print("nhap lai")

