def print_matrix(mat):
    for row in mat:
        print(row)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#2차원 리스트 행 추가
matrix.append([10,11,12])
print("InMatrix after adding a new row:")
print_matrix(matrix)
print()

# 2차원 리스트 행 내 요소 추가 (새 열 추가)
for row in matrix:
    row.append(100) # 각 행의 끝에 100 추가
print("InMatrix after adding a new column:")
print_matrix(matrix)
print()


# 2차원 리스트 삭제 (Delete)
del matrix[2] #세 번째 행 삭제
print("InMatrix after deleting the third row:")
print_matrix(matrix)
print()


# 특정 열 삭제 (예: 모든 행에서 두 번째 열 삭제)
for row in matrix:
    del row[1]  
print("InMatrix after deleting the second column:")
print_matrix(matrix)