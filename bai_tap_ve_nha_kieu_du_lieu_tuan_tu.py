#Bài 1
ds_nguyen_to = []
while True:
    n = input("Nhap vao so nguyen duong n: ")
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break

for i in range(1, n):
    if i == 1:
        ds_nguyen_to.append(i)
        continue
    for j in range(1,i):
        if i%j == 0 and j != 1 and i != j:
            break
    else:
        ds_nguyen_to.append(i)

ds_nguyen_to.sort()
print(ds_nguyen_to)
#Bài 2
ds_so = []
while True:
    n = input("Nhap vao so phan tu n trong danh sach: ")
    if n.isdigit() == False:
       print("Yeu cau nhap lai so nguyen duong!!")
    else:
         n = int(n)
         break
for i in range(n):
    while True:
        so = input(f"Nhap gia tri so thu {i + 1}: ")
        if so.count('-') == 1 and so.replace('-','').isdigit():
            so = float(so)
            break
        else:
            print("Yeu cau nhap vao so!!")
    ds_so.append(so)
tong = sum(ds_so)
print(f"Tong cac so vua nhap: {tong}")
#Bài 3
ds_so_chan = []
ds_so_le= []
while True:
    n = input("Nhap vao so phan tu n trong danh sach: ")
    if n.isdigit() == False:
       print("Yeu cau nhap lai so nguyen duong!!")
    else:
         n = int(n)
         break
for i in range(1,n):
    if i%2==0 :
        ds_so_chan.append(i)
        continue
print(f"Cac số chẵn :{ds_so_chan}")
for j in range(1,n):
    if j%2!=0:
        ds_so_le.append(j)
        continue
print(f"Các số lẻ :{ds_so_le}")
#Bài 4
while True:
    m = input("Nhap vao so cot cua ma tran m = ")
    n = input("Nhap vao so hang cua ma tran n = ")
    if n.isdigit==False or m.isdigit==False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n= int(n)
        m= int(m)
        break
ma_tran_a = []
for hang in range(n):
    phan_tu_trong_hang = []
    for cot in range(m):
        phan_tu_trong_hang.append(0)
    ma_tran_a.append(phan_tu_trong_hang)
print(ma_tran_a)
#Bài 5
while True:
    n = input("Nhap vao n = ")
    if n.isdigit()==False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n= int(n)
        break
ma_tran_don_vi = []
for i in range(n):
    phan_tu_trong_hang = [0]*i + [1] + [0]*(n-1-i)
    ma_tran_don_vi.append(phan_tu_trong_hang)
print(ma_tran_don_vi)
#Bài 6
while True:
    m = input("Nhap vao so cot cua ma tran m = ")
    n = input("Nhap vao so hang cua ma tran n = ")
    if n.isdigit==False or m.isdigit==False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n= int(n)
        m= int(m)
        break
ma_tran_a = []
for hang in range(n):
    phan_tu_trong_hang = []
    for cot in range(m):
        phan_tu_trong_hang.append(0)
    ma_tran_a.append(phan_tu_trong_hang)
lua_chon=None
while lua_chon!=2:
    lua_chon= input("Bạn có muốn chỉnh sửa?(1 để có, 2 để không): ")
    if lua_chon=='1':
        i = input("Nhap vao cot can chinh sua cua ma tran  = ")
        j = input("Nhap vao hang can chinh sua cua ma tran  = ")
        if i.isdigit==False or j.isdigit==False :
            print("Yeu cau nhap lai so nguyen duong!!")
        else:
            i= int(i)
            j= int(j)
        k=int(input("Số cần thay đổi trong ma trận: "))
        ma_tran_a[j][i]=k
        print(ma_tran_a)
    elif lua_chon=='2':
        print("Cảm ơn bạn sử dụng chương trình")
    elif lua_chon!=2 and lua_chon!=1:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại") 
           
#Bài 7
while True:
    m = input("Nhap vao so cot cua ma tran m = ")
    n = input("Nhap vao so hang cua ma tran n = ")
    if n.isdigit==False or m.isdigit==False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n= int(n)
        m= int(m)
        break
ma_tran_a = []
for hang in range(n):
    phan_tu_trong_hang = []
    for cot in range(m):
        phan_tu_trong_hang.append(0)
    ma_tran_a.append(phan_tu_trong_hang)
lua_chon=None
while lua_chon!=2:
    lua_chon= input("Bạn có muốn chỉnh sửa?(1 để có, 2 để không): ")
    if lua_chon=='1':
        i = input("Nhap vao cot can chinh sua cua ma tran  = ")
        j = input("Nhap vao hang can chinh sua cua ma tran  = ")
        if i.isdigit==False or j.isdigit==False:
            print("Yeu cau nhap lai so nguyen duong!!")
        else:
            i= int(i)
            j= int(j)
        k=int(input("Số cần thay đổi trong ma trận: "))
        ma_tran_a[j][i]=k
        print(ma_tran_a)
    elif lua_chon=='2':
        print("Cảm ơn bạn sử dụng chương trình")
    elif lua_chon!=2 and lua_chon!=1:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại") 
e = int(input("Nhap vao hang e: "))
f = int(input("Nhap vao hang f: "))
temp = ma_tran_don_vi[e]
ma_tran_don_vi[e] = ma_tran_don_vi[f]
ma_tran_don_vi[f] = temp
print(ma_tran_don_vi)
#Bài 8
while True:
    m = input("Nhap vao so cot cua ma tran m = ")
    n = input("Nhap vao so hang cua ma tran n = ")
    if n.isdigit==False or m.isdigit==False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n= int(n)
        m= int(m)
        break
ma_tran_a = []
for hang in range(n):
    phan_tu_trong_hang = []
    for cot in range(m):
        phan_tu_trong_hang.append(0)
    ma_tran_a.append(phan_tu_trong_hang)
lua_chon=None
while lua_chon!=2:
    lua_chon= input("Bạn có muốn chỉnh sửa?(1 để có, 2 để không): ")
    if lua_chon=='1':
        i = input("Nhap vao cot can chinh sua cua ma tran  = ")
        j = input("Nhap vao hang can chinh sua cua ma tran  = ")
        if i.isdigit==False or j.isdigit==False:
            print("Yeu cau nhap lai so nguyen duong!!")
        else:
            i= int(i)
            j= int(j)
        k=int(input("Số cần thay đổi trong ma trận: "))
        ma_tran_a[j][i]=k
        print(ma_tran_a)
    elif lua_chon=='2':
        print("Cảm ơn bạn sử dụng chương trình")
    elif lua_chon!=2 and lua_chon!=1:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại") 
e = int(input("Nhap vao hang e: "))
f = int(input("Nhap vao hang f: "))
temp = ma_tran_don_vi[f]
ma_tran_don_vi[f] = ma_tran_don_vi[e]
ma_tran_don_vi[e] = temp
print(ma_tran_don_vi)
#Bài 10
ds_sinh_vien = []
n = int(input("Nhap so sinh vien n = "))
for sinh_vien in range(n):
    print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem sinh vien: "))
    thong_tin_sinh_vien = {"ten":ten,"diem":diem}
    ds_sinh_vien.append(thong_tin_sinh_vien)
#Bài 11
ds_sinh_vien = []
n = int(input("Nhap so sinh vien n = "))
for sinh_vien in range(n):
    print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem sinh vien: "))
    thong_tin_sinh_vien = {"ten": ten,"diem": diem}
    ds_sinh_vien.append(thong_tin_sinh_vien)
print("Ten    Diem")
for sinh_vien in range(n):
    print(f"{sinh_vien['ten']:<7} {sinh_vien['diem']:.1f}")
#Bài 12    
ds_sinh_vien = []
n = int(input("Nhap so sinh vien n = "))
for sinh_vien in range(n):
    print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem sinh vien: "))
    thong_tin_sinh_vien = {"ten": ten,"diem": diem}
    ds_sinh_vien.append(thong_tin_sinh_vien)
print("Ten    Diem")
for sinh_vien in range(n):
    print(f"{sinh_vien['ten']:<7} {sinh_vien['diem']:.1f}")
ten_can_xoa = input("Nhập tên sinh viên cần xóa: ")
for sinh_vien1 in ds_sinh_vien:
    if sinh_vien1["ten"] == ten_can_xoa:
        ds_sinh_vien.remove(sinh_vien1)
        print(f"Đã xóa sinh viên {ten_can_xoa} khỏi danh sách.")
        break
else:
    print(f"Không tìm thấy sinh viên có tên {ten_can_xoa}.")
print("Danh sách sinh viên sau khi xóa:")
for sinh_vien in ds_sinh_vien:
    print(f"{sinh_vien['ten']}   {sinh_vien['diem']}")    
#Bài 13
ds_sinh_vien = []
n = int(input("Nhap so sinh vien n = "))
for sinh_vien in range(n):
    print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem sinh vien: "))
    thong_tin_sinh_vien = {"ten": ten, "diem":diem}
    ds_sinh_vien.append(thong_tin_sinh_vien)
print("Ten    Diem")
for sinh_vien in ds_sinh_vien:
    print(f"{sinh_vien['ten']:<7} {sinh_vien['diem']:.1f}")
tem_moi = input("Nhập tên sinh viên mới: ")
diem_moi = float(input(f"Nhập điểm tổng kết của sinh viên {tem_moi}: "))
found = False
for sinh_vien in ds_sinh_vien:
    if sinh_vien['ten'] == tem_moi:
        found = True
        break
if found:
    print("Thông tin sinh viên đã tồn tại")
else:
    ds_sinh_vien.append({"ten": tem_moi, "diem": diem_moi})
    print("Đã thêm sinh viên")
print("Danh sách sinh viên sau khi thêm:")
for sinh_vien in ds_sinh_vien:
    print(f"{sinh_vien['ten']}   {sinh_vien['diem']}")
#Bài 14
ds_sinh_vien = []
n = int(input("Nhap so sinh vien n = "))
for sinh_vien in range(n):
    print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem sinh vien: "))
    thong_tin_sinh_vien = {"ten": ten, "diem":diem}
    ds_sinh_vien.append(thong_tin_sinh_vien)
print("Ten    Diem")
for sinh_vien in ds_sinh_vien:
    print(f"{sinh_vien['ten']:<7} {sinh_vien['diem']:.1f}")
ten_can_sua = input("Nhập tên sinh viên cần sửa thông tin: ")
tim_ten = False
for sinh_vien in ds_sinh_vien:
    if sinh_vien['ten'] == ten_can_sua:
        tim_ten = True
        diem_moi = float(input(f"Nhập điểm mới cho sinh viên {ten_can_sua}: "))
        sinh_vien['diem'] = diem_moi
        print(f"Đã sửa điểm của sinh viên {ten_can_sua} thành {diem_moi}.")
        break
if not tim_ten:
    print(f"Không tìm thấy sinh viên có tên {ten_can_sua}.")
print("Danh sách sinh viên sau khi sửa:")
for sinh_vien in ds_sinh_vien:
    print(f"{sinh_vien['ten']}   {sinh_vien['diem']}")
#Bài 15
ds_sinh_vien = []
n = int(input("Nhap so sinh vien n = "))
for sinh_vien in range(n):
    print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
    ma_sinh_vien=float(input("Nhap ma sinh vien: "))
    ho_dem= input(" Nhâp họ và tên đệm: ")
    ten = input("Nhap ten sinh vien: ")
    diem_toan = float(input("Nhap diem toan sinh vien: "))
    diem_ly= float(input("Nhap diem ly sinh vien: "))
    diem_hoa= float(input("Nhap diem hoa sinh vien: "))
    diem_trung_binh=(diem_toan+diem_hoa+diem_ly)/3
    thong_tin_sinh_vien = {"ma sinh vien":ma_sinh_vien,"ho dem":ho_dem,"ten": ten, "diem toan":diem_toan, "diem ly":diem_ly,"diem hoa":diem_hoa,"diem trung binh":diem_trung_binh}
    ds_sinh_vien.append(thong_tin_sinh_vien)
print("Mã sinh viên    Họ đệmn    Tên    Điểm toánn    Điểm hoá    Điểm lý    Điểm trung bình")
for student in ds_sinh_vien:
    print(f"{student['ma sinh vien']} {student['ho dem']} {student['ten']}     {student['diem toan']:.1f}     {student['diem hoa']:.1f}     {student['diem ly']:.1f}     {student['diem trung binh']:.1f}")
print("Menu")
print("1. Xem danh sách sinh viên")
print("2. Nhập thông tin sinh viên mới vào danh sách")
print("3. Chỉnh sửa thông tin sinh viên ứng với mã sinh viên")
print("4. Xóa thông tin sinh viên ứng với mã sinh viên")
print("5. Thoát chương trình")
choice = None
while choice != '5':
    choice = input("Nhập lựa chọn của bạn (5 để thoát): ")

    if choice == '1':
        print("Bạn đã chọn: Xem danh sách sinh viên")
        print("Mã sinh viên    Họ đệmn    Tên    Điểm toánn    Điểm hoá    Điểm lý    Điểm trung bình")
        for student in ds_sinh_vien:
            print(f"{student['ma sinh vien']:<7} {student['ho dem']} {student['ten']} {student['diem toan']:.1f} {student['diem hoa']:.1f} {student['diem ly']:.1f} {student['diem trung binh']:.1f}")
    elif choice == '2':
        print("Bạn đã chọn: Nhập thông tin sinh viên mới vào danh sách")
        tem_moi = input("Nhập tên sinh viên mới: ")
        diem_moi = float(input(f"Nhập điểm tổng kết của sinh viên {tem_moi}: "))
        found = False
        for sinh_vien in ds_sinh_vien:
            if sinh_vien['ten'] == tem_moi:
                found = True
                break
        if found:
            print("Thông tin sinh viên đã tồn tại")
        else:
            ds_sinh_vien.append({"ten": tem_moi, "diem": diem_moi})
            print("Đã thêm sinh viên")
        print("Danh sách sinh viên sau khi thêm:")
        for sinh_vien in ds_sinh_vien:
            print(f"{sinh_vien['ten']}   {sinh_vien['diem']}")
    elif choice == '3':
        print("Bạn đã chọn: Chỉnh sửa thông tin sinh viên ứng với mã sinh viên")
        ten_can_sua = input("Nhập tên sinh viên cần sửa thông tin: ")
        tim_ten = False
        for sinh_vien in ds_sinh_vien:
            if sinh_vien['ten'] == ten_can_sua:
                tim_ten = True
                diem_moi = float(input(f"Nhập điểm mới cho sinh viên {ten_can_sua}: "))
                sinh_vien['diem'] = diem_moi
                print(f"Đã sửa điểm của sinh viên {ten_can_sua} thành {diem_moi}.")
                break
        if not tim_ten:
            print(f"Không tìm thấy sinh viên có tên {ten_can_sua}.")
        print("Danh sách sinh viên sau khi sửa:")
        for sinh_vien in ds_sinh_vien:
            print(f"{sinh_vien['ten']}   {sinh_vien['diem']}")
    elif choice == '4':
        print("Bạn đã chọn: Xóa thông tin sinh viên ứng với mã sinh viên")
        ten_can_xoa = input("Nhập tên sinh viên cần xóa: ")
        for sinh_vien1 in ds_sinh_vien:
            if sinh_vien1["ten"] == ten_can_xoa:
                ds_sinh_vien.remove(sinh_vien1)
                print(f"Đã xóa sinh viên {ten_can_xoa} khỏi danh sách.")
                break
        else:
            print(f"Không tìm thấy sinh viên có tên {ten_can_xoa}.")
        print("Danh sách sinh viên sau khi xóa:")
        for sinh_vien in ds_sinh_vien:
            print(f"{sinh_vien['ten']}   {sinh_vien['diem']}")    
    elif choice == '5':
        print("Cảm ơn bạn đã sử dụng chương trình!")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

    