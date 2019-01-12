Km2 = [117.43, 92.24, 43.35, 12.04, 9.96, 10.09]
Dân_số = [150300, 247100, 333300, 266800, 420900, 318000]
Quận = ["ST", "BĐ", "BTL", "CG", "ĐĐ","HBT"]
c = []
for i in range(len(Km2)):
    d = Dân_số[i] // Km2[i]
    c.append(d)
for d in c:
    print("Mật độ dân cư mỗi quận:",d)
a = sum(x for x in c)
print(a)
b = len(Quận)
print(b)
e = a // b
print("Mật độ dân cư trung bình:",e)
