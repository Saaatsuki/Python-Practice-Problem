def create_2d_list(argRow, argCol):
    matrix = []
    for _ in range(argRow):
        row = []
        for _ in range(argCol):
            row.append(None)
        matrix.append(row)
    return matrix

tate = int(input("Enter the number of rows: "))
yoko = int(input("Enter the number of columns: "))

matrix = create_2d_list(tate, yoko)
print(matrix)

for i in range(tate):
    for j in range(yoko):
        val = int(input(f"Enter value for [{i}][{j}]: "))
        matrix[i][j] = val

for row in matrix:
    print(" ".join(f"{val:2}" for val in row))
