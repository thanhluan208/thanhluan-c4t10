a = input("nhập vào một từ :")
b = list(a)
print(b)
from random import shuffle
x = [[i] for i in (b)]
shuffle (x)
for c in x:
    print(*c)