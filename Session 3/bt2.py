a = int(input("a"))
b = int(input("b"))
c = int(input("c"))
if a == 0:
    x = -c/b
    print(x)
else:
    delta = int(b**2 - 4*a*c)
    if delta < 0:
        print("vô nghiệm")
    elif delta == 0:
        x = int(-b/2*a)
        print(x)
    else:
        d = int(delta**1/2*1/2)
        x1 = int(b*1/2 - d )
        x2 = int(-b*1/2 - d )
        print("2 nghiệm phân biệt")
        print(x1)
        print(x2)