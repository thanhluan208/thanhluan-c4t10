a = {
    "năm phát hành" : 2018,
    "diễn viên" : "abc",
    "Nhân vật tham gia" : "xyz",
}
b = {
    "năm phát hành" : 2019,
    "diễn viên" : "ghik",
    "Nhân vật tham gia" : "lmn",
}
c = {
    "năm phát hành" : 2020,
    "diễn viên" : "123456",
    "Nhân vật tham gia" : "98765",
}
d = [a, b, c]
for x in d:
    g = input("Hãng sản xuất:")
    h = input("Quốc gia")
    x["Hãng sản xuất"] = (g)
    x["Quốc gia"] = (h)
print(d)