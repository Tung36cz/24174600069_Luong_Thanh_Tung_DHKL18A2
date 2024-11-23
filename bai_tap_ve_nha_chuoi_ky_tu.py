#Bài 1
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
tach_chuoi = chuoi_nhap_vao.split()
chuoi_ket_qua=len(tach_chuoi)
print(f"Chuoi ket qua :{chuoi_ket_qua}")
#Bài 2
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
tach_chuoi = chuoi_nhap_vao.split()
chuoi_ket_qua = " ".join(tach_chuoi)
print(f"Chuoi ket qua :{chuoi_ket_qua}")
#Bài 3
chuoi_nhap_vao=input("Nhap ho va ten: ")
tach_chuoi = chuoi_nhap_vao.split()
ho="".join(tach_chuoi[0])
tim_ten=len(tach_chuoi)
tim_ten=tim_ten-1
ten="".join(tach_chuoi[tim_ten])
print(f"họ:{ho}, tên:{ten}")
#Bài 4
chuoi_nhap_vao= input("Nhap vao chuoi bat ky: ")
dem_chu = 0
dem_so = 0
dem_ky_tu_dac_biet=0
for chu in chuoi_nhap_vao:
    if chu.isalpha()==True:
        dem_chu = dem_chu
    else:
        if chu.isdigit() == True:
            dem_so= dem_so +1
        else:
            dem_ky_tu_dac_biet= dem_ky_tu_dac_biet + 1
print(f"So chu cai: {dem_chu}")
print(f"So chu cai: {dem_so}")
print(f"So ky tu dac biet: {dem_ky_tu_dac_biet}")
#Bài 5
chuoi_nhap_vao=input("Nhap vao bat chuoi bat ky: ")
dem_chu_viet_hoa=0
dem_chu_viet_thuong=0
for chu in chuoi_nhap_vao:
    if chu.islower()==True:
        dem_chu_viet_thuong=dem_chu_viet_thuong+1
    else:
        if chu.isupper()==True:
            dem_chu_viet_hoa=dem_chu_viet_hoa+1
print(f"Số chữ viết thường: {dem_chu_viet_thuong}")
print(f"Số chữ viết hoa: {dem_chu_viet_hoa}")
#Bài 6
chuoi = input("Nhập chuỗi bạn muốn kiểm tra :")
if chuoi.count('-') == 1 and chuoi.replace('-','').isdigit():
    print("Đây là số âm ")
else :
    print("Đây ko phải số âm ")
#Bài 7
chuoi = input("Nhập chuỗi bạn muốn kiểm tra :")
if chuoi.count('.') == 1 and chuoi.replace('.','').isdigit():
    print("Đây là số thập phân ")
else :
    print("Đây ko phải số thập phân ")
#Bài 8
str_1 = input("Nhập ký tự str_1 :")
str_2= input("Nhập ký tự str_2 :")
if str_1 in str_2:
    print("str_1 nằm trong str_2 ")
elif str_2 in str_1:
    print("str_2 nằm trong str_1")
else:
    print("str_1 không nằm trong str_2")
#Bài 9
chuoi = input("Nhập chuỗi bạn muốn kiểm tra :")
if all(c == '0' or c == '1' for c in chuoi):
    thap_phan = 0
    for i in range(len(chuoi)):
        thap_phan = thap_phan + int(chuoi[i]) * (2 ** (len(chuoi) - 1 - i))    
    print(f"Số thập phân tương ứng là: {thap_phan}")
else:
    print("Số nhị phân không hợp lệ! Chỉ được chứa các ký tự '0' và '1'.")
#Bài 10
chuoi = input("Nhập vào một chuỗi: ")
so = ""
ky_tu_khac = ""
for ky_tu in chuoi:
    if ky_tu.isdigit():  
        so = so + ky_tu
    else:  
        ky_tu_khac = ky_tu_khac + ky_tu
ket_qua = so + ky_tu_khac
print(f"Chuỗi mới sau khi dồn số sang bên trái:{ket_qua}")


