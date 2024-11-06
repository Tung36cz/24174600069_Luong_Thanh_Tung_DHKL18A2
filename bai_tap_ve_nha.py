#Bài 1
for i in range(100):
    if i%2 ==1:
        print(i)
#Bài 2
#S1
tong_s =0
n=int(input("Nhập vào số nguyên dương n: "))
for i in range(n+1):
    tong_s = tong_s+i
    print(f"tong_s lan lap {i}={tong_s}")

print(f"Tổng các số từ 1 đến n = {tong_s}")
#S2
tich_p =1
n=int(input("Nhập vào số nguyên dương n: "))
for i in range(n-1):
    if i==0:
        continue
    tich_p =tich_p*i
    print(f"tong_s lan lap {i}={tich_p}")

print(f"Tổng các số từ 1 đến n = {tich_p}")
#S3
tong =0
n=int(input("Nhập vào số nguyên dương n: "))
for i in range(1,n+1):
   
    tong =tong+((-1)**(i+1)/i)
    print(f"tong_s lan lap {i}={tong:.2f}")

print(f"Tổng các số từ 1 đến n = {tong:.2f}")
#S4
tong=0
n=int(input("Nhập vào số nguyên dương n: "))
for k in range(n+1):
    
    tong =tong+(k/(k+2))
    print(f"tong_s lan lap {k}={tong:.2f}")

print(f"Tổng các số từ 1 đến n = {tong:.2f}")
#Bài 3
a=0
b=1
for i in range(50):
    print(a)
    sum_a_b= a+b
    a=b
    b=sum_a_b
#Bài 4
n= int(input("Nhập vào số nguyên duong cần kiểm tra: "))
if n <= 1:
    print("Số này không phải là số nguyên tố")
else:
    k = n
    for i in range(n):
        if n%k ==0 and k!=n and k!=1:
            print("Số này không phải là số nguyên tố")
            break
        k = k - 1
    else:
        print("Số này là số nguyên tố")        
#Bài 5
n= int(input("Nhập số nguyên dương n: "))
k=0
for i in range(1,n):
   if n%i==0 and n!=i :
       k=k+i
if n==k:
    print(f"{n} là số hoàn hảo")
else:
    print(f"{n} không là số hoàn hảo")
#Bài 6
n= int(input("Nhập số nguyên dương n: "))
for i in range(n):
    if n==i**2:
        print(f"{n} là số chính phương")
        break
else:
    print(f"{n} không là số chính phương")
#Bài 7
n= int(input("Nhập vào số nguyên dương cần kiểm tra: "))
for y in range(1,n):
    k = n
    for i in range(1,y):
        if n%k ==0 and k!=n and k!=1 :
            break
        k = k - 1
    if y>1:
        print(y)

#Bài 8
n = int(input("Nhập vào số nguyên n: "))
for y in range(1, n):
    k = 0
    for i in range(1, y):
        if y % i == 0:
            k=k+i
    if k == y:
        print(y)
#Bài 9
n = int(input("Nhập vào một số nguyên dương n: "))
for i in range(1, n):
    if n>i**2:
        print(i**2) 
#Bài 10
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
so_nho_nhat =a
if b >= a:
    so_nho_nhat = b
k = so_nho_nhat
for i in range(so_nho_nhat):
    if a%k ==0 and b%k == 0:
        print(f"{k} là ước chung lớn nhất")
        break
    k=k-1
#Bài 11
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
if b>=a:
    so_lon_nhat=b
else:
    so_lon_nhat=a
k = so_lon_nhat
for i in range(k):
    if i % a == 0 and i % b == 0 and i!=0:
        print(f"Bội chung nhỏ nhất là: {i}")
        break
#Bài 12
a = int(input("Nhập số tử số: "))
b = int(input("Nhập số mẫu số: "))
so_nho_nhat =a
if b >= a:
    so_nho_nhat = b
k = so_nho_nhat
for i in range(so_nho_nhat):
    if a%k ==0 and b%k == 0:
        
        break
    k=k-1
tu_toi_gian=a//k
mau_toi_gian=b//k
print(f"Kết quả tối giản: {tu_toi_gian}/{mau_toi_gian}")
#Bài 13
n = int(input("Nhập số nguyên: "))
print("1", end="*")
for i in range(2, n + 1):
    while n % i == 0:
        print(i, end="*")
        n = n // i  
#Bài 14
#Tam giác Pascal
n = int(input("Nhập số hàng của Tam giác Pascal: "))
for i in range(n):
    k = [1] * (i + 1)  
    for j in range(1, i):
        k[j] = k[j - 1] + k[j]
    print(" " * (n - i - 1), *k)
#Tam giác Floyd
n = int(input("Nhập số hàng của Tam giác Floyd: "))
k = 1
for i in range(1, n + 1):
    for j in range(i):
        print(k, end=" ")
        k=k+1
    print()  
#Bài 15
#Từ thập phân sang nhị phân
thap_phan = int(input("Nhập số thập phân: "))  
if thap_phan < 0:
    print("Số thập phân phải là một số không âm!")
else:
    nhi_phan = ""
    if thap_phan == 0:
        nhi_phan = "0"
    else:
        while thap_phan > 0:
            nhi_phan = str(thap_phan % 2) + nhi_phan  
            thap_phan = thap_phan // 2  
        print(f"Số nhị phân tương ứng là: {nhi_phan}")
#Từ nhị phân sang thập phân
nhi_phan = input("Nhập số nhị phân: ")
if all(bit in '01' for bit in nhi_phan):  # Kiểm tra tất cả ký tự trong chuỗi
    thap_phan = 0
    for i in range(len(nhi_phan)):
        thap_phan = thap_phan + int(nhi_phan[i]) * (2 ** (len(nhi_phan) - 1 - i))
        
    print(f"Số thập phân tương ứng là: {thap_phan}")
else:
    print("Số nhị phân không hợp lệ! Chỉ được chứa các ký tự '0' và '1'.")
