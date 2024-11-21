#Tính tổng 2 ma trận 
matrix_a = [[0,1,2],
            [4,5,6],
            [7,8,9]]
matrix_b = [[1,2,6],
            [3,8,7],
            [2,8,3]]
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] + matrix_b[hang][cot] 

print(matrix_a)
#Tính ma trận với 1 số
matrix_a = [[0,1,2],
            [4,5,6],
            [7,8,9]]
n = 8
#Nhân ma trận a với n
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] * n

print(matrix_a)
#Tính ma trận nhân ma trận
# Khai báo ma trận A và B
ma_tran_A = [[1,2,6],
             [3,4,8],
             [8,0,1]]

ma_tran_B = [[5,6,7],
             [7,8,0],
             [3,9,1]]
    
hang_A = len(A)
cot_A = len(A[0])
hang_B = len(B)
cot_B = len(B[0])
if cot_A != hang_B:
    print("Số cột của ma trận A phải bằng số hàng của ma trận B.")
ma_tran_C = [[0 for _ in range(cot_B)] for _ in range(hang_A)]
for i in range(hang_A):
    for j in range(cot_B):
        for k in range(cot_A):
            ma_tran_C[i][j] += ma_tran_A[i][k] * ma_tran_B[k][j]
for hang in ma_tran_C:
    print(hang)
