print("How many leg does a spider have?")
print("1. None")
print("2. 4 legs")
print("3. 8 legs")
print("4. 12 legs")
while True:
    a = input("The anwser")
    if a < 0:
        print("The answer must be 1, 2, 3, or 4")
        b = input("enter again")