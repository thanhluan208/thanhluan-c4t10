k = []
print("Phần mêm quản lí nhân viên")
while True:
    name = input("Enter worker's name, seperated by ',':")
    
    a = input("nhập chức vụ:")
    b = input("nhập mức lương")
    c = input("nhập thời hạn hợp đồng")
    d = {
        "Tên nhân viên":(name),
        "chức vụ" : (a),
        "mức lương" : (b),
        "thời hạn hợp đồng" : (c),
    }
    k.append(d)
    # quest = input("Gõ bất cứ nút nào để tiếp tục hoặc gõ quit để dừng lại").lower()
    # if quest == "quit":
    #     break
    for i in k:
        if i == 1:
            print(i)
            break
print(k)