check = 0 
danhsach = []
current_id = 101

while check != 5 :
    print("="*75)
    print("QUẢN LÝ NHÂN SỰ - STAFF MANAGER")
    print("="*75)
    print(
"""
1. Thêm nhân viên mới
2. Danh sách nhân viên
3. Tìm kiếm nhân viên (theo mã)
4. Xóa nhân viên khỏi hệ thống
5. Thoát chương trình
"""
    )
    print("="*75)
    check = input("Nhập lựa chọn của bạn : ").strip()
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
                else:
                    try:
                        luong = float(luong)
                        if luong <= 0:
                            print("Mức lương phải là số dương (> 0) ! Vui lòng nhập lại")
                        else:
                            break
                    except ValueError:
                        print("Lương nhập không hợp lệ ! Vui lòng nhập lại")

            new = {
                'id': current_id,
                'name': ten,
                'salary': luong
            }
            danhsach.append(new)
            print(f"Thêm nhân viên thành công! ID: {current_id}")
            current_id += 1
            
        case "2" : 
            if len(danhsach) == 0 :
                print("Chưa có dữ liệu nhân sự!")
            else : 
                print(f"{'ID' :<5} | {'Tên Nhân Viên' :<20} | {'Mức Lương' :<10}")
                print("-" * 45)
                for j in danhsach : 
                    print(f"{j['id'] :<5} | {j['name'] :<20} | {j['salary'] :<10}")

        case "3" : 
            while True : 
                timid = input("Nhập ID cần tìm kiếm : ").strip()
                if timid == "" :
                    print("ID không được để trống ! Vui lòng nhập lại ")
                elif not timid.isdigit():
                    print("ID không hợp lệ ! Vui lòng nhập lại")
                else : 
                    timid = int(timid)
                    break
            
            for j in danhsach : 
                if j['id'] == timid : 
                    print("Thông tin chi tiết:")
                    print(j)
                    break 
            else : 
                print(f"Không tìm thấy nhân viên có ID {timid}!")
        
        case "4" : 
            while True : 
                timid = input("Nhập ID nhân viên cần xóa : ").strip()
                if timid == "" :
                    print("ID không được để trống ! Vui lòng nhập lại ")
                elif not timid.isdigit():
                    print("ID không hợp lệ ! Vui lòng nhập lại")
                else : 
                    timid = int(timid)
                    break
                    
            for j in danhsach : 
                if j['id'] == timid : 
                    danhsach.remove(j)
                    print(f"Đã xóa nhân viên ID {timid} thành công!")
                    break 
            else : 
                print("Không tìm thấy nhân viên để xóa!")
        
        case "5" :
            print("Kết thúc chương trình")
            break 
        case _:
            print("Lựa chọn không hợp lệ ! Vui lòng nhập lại ")
