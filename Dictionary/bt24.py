a = {
    "DELL" : 20, 
    "HP" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}
b = input("Tên hãng máy tính :")
c = int(input("Số lượng:"))
a[b] = (c)
a ["DELL"] = 60
a ["MACBOOK"] = 10
for i in a:
    print (i)

c = sum (a.values())
print(c)
a ["FUJITSU"] = 15
a ["ALIENWARE"] = 5