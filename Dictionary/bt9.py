a = ["huy", "tung", "m.duc"]
print("Name:",a)
b = {
    "Role" : "Waiter",
    "Hour" : 12,
    "Salary per Hour ($)" : 0.8
}
c = {
    "Role" : "cook",
    "Hour" : 24,
    "Salary per Hour ($)" : 1.5 
}
d = {
    "Role" : "Manager",
    "Hour" : 20,
    "Salary per Hour ($)" : 2
}
e = input("enter a name:")
g = e.lower()
if g == "huy":
    print(b)
elif g =="tung":
    print(c)
elif g == "m.duc":
    print(d)
# else:
#     print("...")
a.append("don")
a.append("h.duc")
print("name':", a)
h = {
    "Role" : "Waiter",
    "Hour" : 12,
    "Salary per Hour ($)" : 0.9
}
i = {
    "Role" : "Waiter",
    "Hour" : 14,
    "Salary per Hour ($)" : 0.7
}
