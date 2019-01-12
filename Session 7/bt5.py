a = [5, 1, 8, 22, 44, 16, 8,]
b = int(input("enter a number:"))

if b in a:
    c = a.index(b)
    print("found,", "position:", c + 1 )
    
else:
    print("not found")