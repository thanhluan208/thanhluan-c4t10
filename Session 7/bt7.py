a = input("enter a list of number, seperated by ' ': ")
b = a.split(" ")
print(*b)
c = sum(int(x) for x in b)
print(c)


# l_int = []
# for x in b:
# l_int.append(int(x))

