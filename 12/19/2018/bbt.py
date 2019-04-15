while True:
    c = input("Email :")
    if "@" and "." in c:
        f = c.count("") -1
        if f > 8:
            print("Đăng kí thành công")
            break
        else:
            print("vui lòng nhập lại email:")
    else:
        print("vui lòng nhập lại email:")