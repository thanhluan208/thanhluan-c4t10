a = [45, 67, 56, 78]
c = int(input("enter your new highscore:"))
a.append(c)
b = sorted(a, reverse = True)
for i, d in enumerate(b):
    print(i,d)