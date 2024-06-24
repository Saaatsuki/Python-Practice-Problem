import random

# 구구단 출력 함수
# a부터 b까지의 구구단을 출력한다. b가 지정되지 않으면 a의 구구단만 출력한다.
def mul(a, b = None):
    # b가 None인 경우, a의 다음 숫자로 설정
    b = a + 1 if b is None else b + 1
    # a부터 b-1까지의 구구단 출력
    for i in range(a, b):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")
        print()

# 랜덤값 삼각형 출력 함수
# 높이가 h인 삼각형을 랜덤한 숫자로 채워서 출력한다.
def tri(h):
    # 0부터 9까지의 리스트 생성
    num_list = [i for i in range(10)]
    # 높이 h만큼의 삼각형 출력
    for j in range(h):
        empty = h - j - 1  # 왼쪽 공백의 개수 계산
        for _ in range(j + 1):
            # 리스트에서 랜덤한 숫자 선택
            ran_num = random.choice(num_list)
            # 선택된 숫자를 리스트에서 제거
            num_list.remove(ran_num)
            # 삼각형의 왼쪽 공백 출력
            print(" " * empty, end="")
            # 랜덤한 숫자 출력
            print(ran_num, end="")
            empty = 0  # 공백 초기화
        print()

# 메인 프로그램 루프
while True:
    # 메뉴 출력
    print("--------------------\n1. 구구단 출력\n2. 랜덤값 삼각형 출력\n3. 종료\n--------------------")

    # 사용자로부터 메뉴 번호 입력 받기
    menu = int(input("원하는 메뉴 번호를 입력하세요: "))

    if menu == 1:
        range_flag = False
        while not range_flag:
            # 구구단 범위 입력 받기
            ran = input("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)\n")
            if "~" in ran:
                # 범위가 지정된 경우
                ran = list(map(int, ran.split("~")))
                # 범위가 올바른지 확인
                if not (2 <= ran[0] <= 9) or not (2 <= ran[1] <= 9):
                    range_flag = False
                else:
                    range_flag = True
                    n1 = ran[0]
                    n2 = ran[1]
                    mul(n1, n2)
            else:
                # 범위가 지정되지 않은 경우
                ran = int(ran)
                # 숫자가 올바른지 확인
                if not 2 <= ran <= 9:
                    range_flag = False
                else:
                    range_flag = True
                    mul(ran)

    elif menu == 2:
        # 삼각형 높이 입력 받기
        h = int(input("삼각형의 높이 줄 수를 입력하세요(2이상 3이하)\n"))
        while h != 2 and h != 3:
            h = int(input("삼각형의 높이 줄 수를 입력하세요(2이상 3이하)\n"))
        tri(h)

    elif menu == 3:
        # 프로그램 종료
        print("프로그램을 종료합니다.")
        break

    else:
        # 잘못된 메뉴 번호 입력 시 메시지 출력
        print("1~3 사이의 값을 입력하세요")
        