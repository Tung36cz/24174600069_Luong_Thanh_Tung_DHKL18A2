#Bài 1
nam = float(input("Nhập số năm: "))
if nam >= 0:
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print ("Là năm nhuận ")
    else:
        print("Không là năm nhuận")
else:
    print("Không tồn tại bài toán")
print("Kết thúc chương trình")
    
#Bài 2
x=float(input("Nhập toạ độ x trên M: "))
y=float(input("Nhập toạ độ y trên M: "))
a=float(input("Nhập toạ độ a của tâm I: "))
b=float(input("Nhập toạ độ b của tâm I: "))
R=float(input("Nhập toạ độ bán kính R: "))
khoang_cach_cua_M_va_I= ((x-a)*2+(y-b)*2)**1/2
R_gioi_han=R**2
if khoang_cach_cua_M_va_I <= R_gioi_han:
    print("True")
else:
    print("False")
    
#Bài 3
a=float(input("Nhập số a: "))
b=float(input("Nhập số b: "))
c=float(input("Nhập số c: "))
if a>b and a>c:
    print("a là số lớn nhất")
elif b>a and b>c:
    print("b là số lớn nhất")
elif c>a and c>b:
    print("c là số lớn nhất")
elif a==b and a>c:
    print("a và b là 2 số lớn nhất")
elif a==b and c>a:
    print("c là số lớn nhất")
elif b==c and b>a:
    print("b và c là 2 số lớn nhất ")
elif b==c and a>b:
    print("a là số lớn nhất")    
elif a==c and a>b:
    print("a và c là 2 số lớn nhất")
elif a==c and b>a:
    print("b là số lớn nhất") 
    
#Bài 4
a=float(input("Nhập độ dài a: "))
b=float(input("Nhập độ dài b: "))
c=float(input("Nhập độ dài c: "))
if a>0 and b>0 and c>0:
    if (a**2 + b**2)==c**2 or (a**2+c**2)==b**2 or (b**2+c**2)==a**2:
        print("Là tam giác vuông")
    elif (a==b and a!=c) or (a==c and a !=b) or (b==c and b!=c):
        print("Là tam giác cân")
    elif ((a**2+b**2)==c**2 and a==b)or ((a**2+c**2)==b**2 and a==c) or ((b**2+c**2)==a**2 and b==c):
        print("Là tam giác vuông cân")
    elif a==b==c:
        print("Là tam giác đều")
    else:
        print("là tam giác thường")
else:
    print("Không tồn tại bài toán")
  
#Bài 5  
ky_tu = input("Nhập một ký tự: ")
if len(ky_tu) != 1 or not ky_tu.isalpha():
    print("Vui lòng nhập một ký tự hợp lệ.")
else:
    if ky_tu in 'aeiou':
        print(f"{ky_tu} là nguyên âm.")
    else:
        print(f"{ky_tu} là phụ âm.")

#Bài 6
print("----- Chọn thể loại phim -----")
print("1. Phim tình cảm")
print("2. Phim kinh dị")
print("3. Phim hoạt hình")
print("4. Phim khoa học viễn tưởng")
print("0. Thoát")
choice = None
while choice != '0':
    choice = input("Nhập lựa chọn của bạn (0 để thoát): ")

    if choice == '1':
        print("Bạn đã chọn: Phim tình cảm")
    elif choice == '2':
        print("Bạn đã chọn: Phim kinh dị")
    elif choice == '3':
        print("Bạn đã chọn: Phim hoạt hình")
    elif choice == '4':
        print("Bạn đã chọn: Phim khoa học viễn tưởng")
    elif choice == '0':
        print("Cảm ơn bạn đã sử dụng chương trình!")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

#Bài 7
a_1=float(input("Nhập độ dài a1: "))
a_2=float(input("Nhập độ dài a2: "))
b_1=float(input("Nhập độ dài b1: "))
b_2=float(input("Nhập độ dài b2: "))
c_1=float(input("Nhập độ dài c1: "))
c_2=float(input("Nhập độ dài c2: "))
D= a_1*b_2 - a_2*b_1
Dx= c_1 * b_2 - c_2 * b_1
Dy = a_1 * c_2 - a_2 * c_1
if D == 0:
    if Dx == 0 and Dy == 0:
        print("Hệ phương trình có vô số nghiệm")
    else:
        print("Hệ phương trình vô nghiệm")
else:
    x = Dx / D
    y = Dy / D
    print(f"Nghiệm của hệ phương trình là: x = {x}, y = {y}")

#Bài 8
diem=str(input("Nhập số điểm: "))
if diem in 'A':
    print("Sinh viên xuất sắc")
elif diem in 'B':
    print("Sinh viên loại giỏi")
elif diem in 'C':
    print("Sinh viên khá")
elif diem in 'D':
    print("Sinh viên loại trung bình ")
elif diem in 'E':
    print("Sinh viên loại yếu")
elif diem in 'F':
    print("Sinh viên xếp loại kém")
else:
    print("Xin vui lòng nhập lại")

#Bài 9
loai_xe = int(input("Nhập loại xe (4 hoặc 7): "))
km = float(input("Nhập khoảng cách di chuyển (km): "))
thoi_gian_cho = int(input("Nhập thời gian chờ (phút): "))
if loai_xe == 4:
    cuoc_phi = 11000 / 0.8
    if km <= 0.8:
        cuoc_phi = 11000  
    elif km <= 20:
        cuoc_phi = (km - 0.8) * 12100
    else:
        cuoc_phi = (20 - 0.8) * 12100 + (km - 20) * 10000
elif loai_xe == 7:
    cuoc_phi = 13000 / 0.8
    if km <= 0.8:
        cuoc_phi = 13000  
    elif km <= 30:
        cuoc_phi = (km - 0.8) * 14100
    else:
        cuoc_phi = (30 - 0.8) * 14100 + (km - 30) * 12000
else:
    print("Loại xe không hợp lệ. Vui lòng nhập 4 hoặc 7.")
    exit()

if thoi_gian_cho > 5:
    thoi_gian_cho <= 5 
    cuoc_phi = thoi_gian_cho * 800

print(f"Cước phí taxi là: {cuoc_phi:.0f} đồng")

#Bài 10
luong= int(input("Nhập luơng (triệu đồng): "))
if luong >= 0:
    if luong > 15:
        luong_rong= luong*(30/100)
    elif luong >= 7 and luong <= 15:
        luong_rong= luong*(20/100)
    elif luong < 7:
        luong_rong= luong*(10/100)
else:
    print("Sai số tiền, vui lòng nhập lại")
print(f"Lương tháng này là: {luong_rong:.1f} triệu đồng")
            