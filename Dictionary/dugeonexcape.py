from random import randint
z = int(input("chiều dài của map"))
o = int(input("chiều rộng của map"))
while True:
    end = {
        "m" : randint(0, o-1),
        "n" : randint(0, z-1)
    }
    key = {
        "h" : randint(0, o-1),
        "g" : randint(0, z-1),
    }
    player = {
        "x" : randint(0, o-1),
        "y" : randint(0, z-1),
        "key" : 0
    }
    if end["m"] != key["h"] and end["m"] != player["x"] and player ["x"] != key["h"]:
        print(end["m"])
        print(end["n"])

        print(key["h"])
        print(key["g"])
        print(player["y"])
        print(player["x"])
        break

while True:
    
    for y in range(z):
        for x in range (o):
            if x == player["x"] and y == player["y"]:
                print("P", end="")
            elif x == key["h"] and y == key["g"]:
                  print("K", end="")
            elif x == end["m"] and y == end["n"]:
                 print("E", end="")
            else:
                print("-", end="")
        print("")
    clone = {
        "x" : player["x"],
        "y" : player["y"]
    }
    a = input ("chọn W D S A để di chuyển").lower()
    if a == "w":
        clone["y"] = clone["y"] - 1
    elif a == "d":
        clone["x"] = clone["x"] + 1
    elif a == "s":
        clone["y"] = clone["y"] + 1
    elif a == "a":
        clone["x"] = clone["x"] - 1
    if clone["x"] in range(z) and clone["y"] in range(o):
        player["x"] = clone["x"]
        player["y"] = clone["y"]
    if player["x"] == key["h"] and player["y"] == key["g"]:
        print("Bạn đã tìm được chìa khóa")
        player["key"] = 1
        key["g"] = key["g"] -3
    if player["x"] == end["m"] and player["y"] == end["n"] and player["key"] == 1:
        print("WINNN!!!")
        break
    if player["x"] == end["m"] and player["y"] == end["n"] and player["key"] == 0 :
        print("Chưa có key","hãy đi tìm key")
    if player["x"] == key["h"]:
        print("bạn đã đến đúng cột có key")
    if player["y"] == key["g"]:
        print("bạn đã đến hàng chứa key")