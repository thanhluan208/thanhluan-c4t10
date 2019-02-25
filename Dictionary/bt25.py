import random
Character = {
    "Name" : "Light",
    "Age" : 17,
    "Strength" : 8,
    "Defense": 10,
    "HP": 100,
    "Backpack": "Shield, Bread Loaf",
    "Gold": 100,
    "Level": 2,
}
Character ["Gold"] = 50
Character ["Backpack"] = "FlintStone"
Character ["Pocket"] = "MonsterDex", "Flashlight"

skill1 = {
    "Name": "Tackle",
    "Minimum level": 1,
    "Damage": 5,
    "Hit rate": 0.3  , 
}
skill2 = {
    "Name": "Quick attack",
    "Minimum level": 2,
    "Damage": 3,
    "Hit rate": 0.5,
}
skill3 ={
    "Name": "Strong Kick",
    "Minimum level": 4,
    "Damage": 7,
    "Hit rate": 0.2,
}
d = [skill1, skill2, skill3]
for i in d:
    print(i["Name"])
lvl_character = 2
a = input ("chọn một skill skill1, skill2, skill3:")
if a == "skill1":
    if lvl_character < skill1["Minimum level"]:
        print("Chưa đủ level")
    elif lvl_character >= skill1["Minimum level"]:
        a = random.uniform(0, 1)
        if a < skill1["Hit rate"]:
            print("skill trượt")
        elif a >= skill1["Hit rate"]:
            print("bạn đã gây ra", (skill1["Damage"]),"damage")
elif a == "skill2":
    if lvl_character < skill2["Minimum level"]:
        print("Chưa đủ level")
    elif lvl_character >= skill2["Minimum level"]:
        a = random.uniform(0, 1)
        if a < skill2["Hit rate"]:
            print("skill trượt")
        elif a >= skill2["Hit rate"]:
            print("bạn đã gây ra", (skill2["Damage"]),"damage")
elif a == "skill3":
    if lvl_character < skill3["Minimum level"]:
        print("Chưa đủ level")
    elif lvl_character >= skill3["Minimum level"]:
        a = random.uniform(0, 1)
        if a < skill3["Hit rate"]:
            print("skill trượt")
        elif a >= skill3["Hit rate"]:
            print("bạn đã gây ra", (skill3["Damage"]),"damage")