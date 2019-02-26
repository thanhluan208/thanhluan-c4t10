# from random import randint
# a = randint(0, 10)
# print(a)
for x in range (4):
    for y in range (4):
        if x == 2 and y == 3:
            print("K", end="")
        else:
            print("-", end="")
    print("")