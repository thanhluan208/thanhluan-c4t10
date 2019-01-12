b = ["blue", "red", "teal", "green"]
a = input("nhập vào một vị trí hoặc một nội dung:")
if a.isdigit:
    while True:
        if 0 <= a <= len(b):
            b.pop(a)
            print(*b)
            break
        else:
            print("Nhập lại đúng vị trí")
else:
    b.remove(a)
    print(*b)