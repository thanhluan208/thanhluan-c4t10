a  = [ 23, 45, 64, 32, 33, 55, 89, 1]
b = int(input("enter your new highscore:"))
a.append(b)
c = sorted(a, reverse = True)
i = 0
for i in range(0,5):
    print(c[i])