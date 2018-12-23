from random import randint
f = 0
while True:
    if f > 5:
        x = int(randint(0, 100))
        y = int(randint(0, 100))
        z = int(randint(-1, 1))
    else:
        x = int(randint(0, 10))
        y = int(randint(0, 10))
        z = int(randint(-1, 1))
    a = x + y + z
    print(f"{x} + {y} = {a}")
    if z == -1 or z == 1:
        check = 0
    elif z == 0:
        check = 1
    while True:
        c = input("chọn Y hoặc N : ")
        if c == "Y" and check == 1:
            print("đúng")
            f = f + 1
            print("Điểm : ",f)
            break
        elif c == "Y" and check == 0:
            print("sai")
            check = 2
            print("total max : ",f)
            break
        elif c == "N" and check == 0:
            print("Đúng")
            f = f + 1
            print("Điểm : ",f)
            break
        elif c =="N" and check == 1:
            print("Sai")
            check = 2
            print("total max : ",f)
            break
        else:
            print("vui lòng nhập lại * chỉ được nhập Y hoặc N ^_^ ")
    if check == 2:
        break
    