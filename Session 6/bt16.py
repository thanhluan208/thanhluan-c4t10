from random import choice, shuffle
g = 0
while True:
    a = ["fornite", "Lol", "PUBG", "Dota"]
    x = choice(a)
    y = [i for i in (x)]
    shuffle (y)
    print(*y)
    e = input("sắp xếp thành 1 từ có nghĩa :")
    if e == x:
        g = g + 1
        print("đúng", g)
    else:
        print("sai", g)
        break
