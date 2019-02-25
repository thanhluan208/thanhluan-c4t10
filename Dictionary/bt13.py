b = []
a = {
    "name" : "huy",
    "Role" : "Waiter",
    "Hour" : 12,
    "Salary per Hour ($)" : 0.8
}
c = {
    "name" : "don",
    "Role" : "cook",
    "Hour" : 24,
    "Salary per Hour ($)" : 1.5 
}
d = {
    "name" : "m.duc",
    "Role" : "Manager",
    "Hour" : 20,
    "Salary per Hour ($)" : 2
}
b = [a, c, d]
b.pop(2)
print(b)