print (" Đăng kí tài khoản ở đây ^_^")
a = input("Tên đăng nhập :")
b = input("Mật khẩu :")
while True:
    print("Nhập lại mật khẩu")
    d = input("mật khẩu:")
    e = input("Nhap lai mat khau")
    if d == e:
        break
    else:
        print("vui lòng nhập lại email:")
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
        print("vui lòng nhập lại email")