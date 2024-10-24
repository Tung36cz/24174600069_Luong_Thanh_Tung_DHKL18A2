#Bài 1
r = float(input("Nhap vao so r: "))
h = float(input("Nhap vao so h: "))
if h>0 and r>0:
    pi = 3.14
    dien_tich_xung_quanh = 2*pi*r*h
    dien_tich_toan_phan = 2*pi*r*h + 2*pi*r**2
    the_tich = pi*r**2*h
    print(f"dien_tich_xung_quanh: {dien_tich_xung_quanh:.2f}")
    print(f"dien_tich_toan_phan: {dien_tich_toan_phan:.2f}")
    print(f"the_tich: {the_tich:.2f}")
else:
    print("gia tri nhap khong thoa man")
print("ket thuc chuong trinh")

#Bài 2
x = float(input("Nhap vao so x: "))
if (x**4+1)**(1/7) != 0:
    y= (-x+(x**2+4)**(1/2))/(x**4+1)**(1/7)
    print(f"y: {y:.2f}")
else:
    print("Gia tri nhap khong hop le")
print("Ket thuc chuong trinh")
#Bài 4
t  = int(input("Nhap thoi gian su dung bong den (s): "))
U = 220
I = 2.7
if t>0:
    P= (t*U*I)/(3600*1000)
    tien_phai_tra = P * 7000 
    print(f"Tien dien phai tra: {tien_phai_tra}")
else:
    print("bai toan khong ton tai")
print("ket thuc chuong trinh")

#Bài 8
import math 
x = float(input("Nhap vao so x: "))
if x>0:
    y = math.log(4,x) + math.log(x,2)
    print(f"y: {y:.2}")
else: 
    print("Bai toan khong ton tai")
print("Ket thuc chuong trinh")
