n1, n2 = map(int, input().split())

matrix_A = []
matrix_B = []


for i in range(n1):
    matrix_A.append(list(map(int, input().split())))


for i in range(n1):
    matrix_B.append(list(map(int, input().split())))


for i in range(n1):
    result_row = []
    for j in range(n2):
        result_row.append(matrix_A[i][j] + matrix_B[i][j])
    print(" ".join(map(str, result_row)))
