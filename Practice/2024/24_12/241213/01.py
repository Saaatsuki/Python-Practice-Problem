ID = 0
li3 = []

def display_menu():
    print("\n\n===== 메뉴 =====")
    print(f"현재 매트릭스 수 : {ID}")
    print("1. 매트릭스 생성")
    print("2. 생성된 매트릭스 출력")
    print("3. 2차원 배열로 변환 후 출력")
    print("4. 매트릭스 삭제")
    print("5. 종료")
    return get_menu_selection()

def get_menu_selection():
    while True:
        try:
            menu = int(input("메뉴 선택 : "))
            if 1 <= menu <= 5:
                return menu
            print("메뉴 값을 1 ~ 5 사이 정수를 입력하세요.")
        except ValueError:
            print("정수를 입력하세요.")

def get_input_in_range(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"{min_val} 이상 {max_val} 이하 값을 입력하세요.")
        except ValueError:
            print("정수를 입력하세요.")

def create_matrix():
    global ID, li3
    rows = get_input_in_range("매트릭스의 행(row) 수를 입력하세요 (1~10) : ", 1, 10)
    cols = get_input_in_range("매트릭스의 열(col) 수를 입력하세요 (1~10) : ", 1, 10)

    value = (ID + 1) * 10 + 1
    matrix = [[value + col + row * cols for col in range(cols)] for row in range(rows)]

    li3.append(matrix)
    ID += 1
    print(f"매트릭스(ID:{ID})가 생성되었습니다.")

def display_matrices():
    if not li3:
        print("Matrix가 없습니다.")
        return

    for idx, matrix in enumerate(li3, start=1):
        print(f"매트릭스 (ID : #{idx}) :")
        print_2d_array(matrix)

def display_as_2d_arrays():
    if not li3:
        print("Matrix가 없습니다.")
        return

    for idx, matrix in enumerate(li3, start=1):
        print(f"2차원 배열 (ID : #{idx}) :")
        print_2d_array(matrix)

def delete_matrix():
    global ID, li3
    if not li3:
        print("Matrix가 없습니다.")
        return

    del_id = get_input_in_range("삭제할 매트릭스 ID를 입력하세요 : ", 1, ID)
    del li3[del_id - 1]
    ID -= 1
    print(f"매트릭스(ID:{del_id})가 삭제되었습니다.")

def print_2d_array(matrix):
    for row in matrix:
        print(" ".join(f"{val:2d}" for val in row))

def run():
    while True:
        menu = display_menu()
        if menu == 1:
            create_matrix()
        elif menu == 2:
            display_matrices()
        elif menu == 3:
            display_as_2d_arrays()
        elif menu == 4:
            delete_matrix()
        elif menu == 5:
            print("프로그램을 종료합니다.")
            break

if __name__ == "__main__":
    run()
