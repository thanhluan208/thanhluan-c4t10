a = str(input("Username?"))
print(a)
if a == "techkid":
    b = input("password")
    if b == "codethechange":
        print("Welcome,superuser")
    else:
        print("password invalid")
else:
    print("You are not superuser")