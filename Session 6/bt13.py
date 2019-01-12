f = []
while True:

    a = input("Chọn một trong 4 thao tác CRUD :")
    if a == "C" or a == "c":
        b = input("Thêm một thứ mà bạn yêu thích :")
        f.append(b)
        print(f)
    elif a == "R" or a == "r":
        print(f)
        if len(f) == 0:
            print("danh sách rỗng")
        else:
            print(f)
    elif a == "U" or a == "u":
        while True:
            c = int(input("vị trí  muốn cập nhật :"))
            d = input("nội dung muốn cập nhật")
            if 0 <= c <= len(f) :
                f [c] = d
                print(f)
                break
            elif c < 0 or c > len(a):
                print("Vui lòng nhập lại")
    elif a == "d" or a =="D":
        while True:
            e = int(input("vị trí muốn xóa :"))
            if 0 <= e <= len(a) :
                a.pop(e)
                print(f)
                break
            elif e < 0 or e > len(a):
                print("Vui lòng nhập lại")
    else:
        print("vui lòng nhập lại :")
    g = input("quit để dừng hoặc ấn một phím để tiếp tục :")
    if g == "quit" or g == "Quit":
        break