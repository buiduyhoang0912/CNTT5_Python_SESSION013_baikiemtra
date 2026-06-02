check = 0 
danhsach = []
while check != 5 :
    print("="*75)
    print("QUẢN LÝ NHÂN SỰ -STAFF MANAGER")
    print("="*75)
    print(
"""
1. Thêm nhân viên mới
2. Danh sách nhân viên
3. Tìm kiêm nhân viên (theo mã)
4. Xóa nhân viên khỏi hệ thông
5. Thoát chương trình
"""
    )
    print("="*75)
    check = input("Nhập lựa chọn của bạn : ")
    match check : 
        case "1": 
            while True : 
                ten = input("Nhập tên nhân viên : ").strip().title()
                if ten == "":
                    print("Tên không được để trống ! Vui lòng nhập lại")
                else : 
                    break 
            
            while True : 
                luong = input("Nhập mức lương của bạn : ").strip()
                if luong == "" :
                    print("Lương không được để trống ! Vui lòng nhập lại")
                elif not luong.isdigit() :
                    print("Lương nhập không hợp lệ ! Vui lòng nhập lại ")
                else : 
                    luong = float(luong)
                    break 

            new ={
                "Tên Nhân Viên" : ten,
                "Mức Lương" : luong
            }
            danhsach.append(new)
        case "2" : 
            if len(danhsach) == 0 :
                print("Chưa có dữ liệu nhân sự!")
            else : 
                print(f"{'ID' :<4} | {'Tên Nhân Viên' :<10} | {'Mức Lương' :6}")
                for i, j in enumerate(danhsach,start=1) : 
                    print(f"{100 + int(i) :<4} | {j['Tên Nhân Viên'] :<10} | {j['Mức Lương'] :6}")

        case "3" : 
            while True : 
                timid = input("Nhập ID ần tìm kiếm : ").strip()
                if timid == "" :
                    print("ID không được để trống ! Vui lòng nhập lại ")
                elif not timid.isdigit():
                    print("ID khôgn hợp lệ ! Vui lòng nhập lại")
                else : 
                    timid = int(timid)
                    break
            
            for i,j in enumerate(danhsach,start =1) : 
                i = 100 + int(i)
                if i == timid : 
                    print(f'Thông tin nhân viên')
                    print(f"'id' : {i} ,{j}")
                    break 
            else : 
                print("Không tìm thấy nhân viên ")
        
        case "4" : 
            while True : 
                timid = input("Nhập ID ần tìm kiếm : ").strip()
                if timid == "" :
                    print("ID không được để trống ! Vui lòng nhập lại ")
                elif not timid.isdigit():
                    print("ID khôgn hợp lệ ! Vui lòng nhập lại")
                else : 
                    timid = int(timid)
                    break
            for i,j in enumerate(danhsach,start =1) : 
                i = 100 + int(i)
                if i == timid : 
                    danhsach.remove(j)
                    print(f"Đã xóa thành công nhân viên ID {i} thành công !")
                    break 
            else : 
                print("Không tìm thấy nhân viên ")
        
        case "5" :
            print("Kết thúc chương trình")
            break 
        case _:
            print("Lựa chọn không hợp lệ ! VUi lòng nhập lại ")

