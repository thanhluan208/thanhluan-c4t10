a = [5, 1, 8, 92, 7, 30]
for b in a:
    c = b % 2
    if c == 0:
        d = a.index(b)
        print("Số chẵn:",b , "position:", d + 1 )
    
