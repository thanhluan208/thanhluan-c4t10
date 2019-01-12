a = input("Enter a list of number, seperate by ',':")
b = a.split(",")
for c in b:
    d = int(c) % 2
    if d == 0:
        print("số chắn:", c)
