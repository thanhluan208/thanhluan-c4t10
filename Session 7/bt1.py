a = ["blue", "red", "teal", "green"]
print("our color list:", *a)
b = input("enter new color :")
a.append(b)
print("our color list:", *a)