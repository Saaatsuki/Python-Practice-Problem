# 매뉴 출력 (1 ~ 3) 이외의 값이 들어올 경우 에러 메시지 출력 후 재입력 요구
def menu():
    while True:
        print("--------------------")
        print("1. 구구단 출력")
        print("2. 랜덤값 삼각형 출력")
        print("3. 종료")
        print("--------------------")
        user_menu_input = int(input("원하는 메뉴 번호를 입력하세요: "))
        if user_menu_input == 1:
            gugudan()
        elif user_menu_input == 2:
            triangle()
        elif user_menu_input == 3:
            print("프로그램을 종료합니다.")
            break
        else:
            print("1~3 사이의 값을 입력하세요")

# 1. 구구단 출력 (2 ~ 9) 이외의 값이 들어올 경우 에러 메시지 출력 후 재입력 요구
def gugudan():
    # 입력값이 ~이 포함이 되어있나 안되어있나 구분
    while True:
        while True:
            user_input =input("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)\n")
            user_input_list = []
            for i in user_input:
                if i != "~":
                    i = int(i)
                    user_input_list.append(i)
                    
            if len(user_input_list) <= 3 and 1 not in user_input_list:
                break
            else:
                print("2~9 사이의 값으로 입력하세요")                
       
    
        # ~이 없을때
        if len(user_input_list) == 1:
            for i in user_input_list:
                for j in range(1, 10):
                    print(f"{i} * {j} = {i * j}")
        
        # ~이 있을때
        elif len(user_input_list) == 2:
            i, j = user_input_list
            for a in range(i, j+1):
                for b in range(1, 10):
                    print(f"{a} * {b} = {a * b}")
                print("")
        break

# 2. 랜덤값 삼각형 출력
def triangle():
    import random
    # 사용자로부터 삼각형 높이(2~3줄)을 입력 받음
    while True:
        high = int(input("삼각형의 높이 줄 수를 입력하세요(2 이상 3이하)\n"))
        
        # 2~3줄 일때
        if 2 <= high <= 3:
            break

        # 아닐때
        print("2 또는 3을 입력하세요")
    
    # 높이 2
    if high == 2:
        alist = []
        count = 0
        while count < 3:
            a = random.randint(1, 9)
            if a not in alist:
                alist.append(a)
                count += 1

        print(f"{" "}{alist[0]}")
        print(f"{alist[1]}{alist[2]}")
                
    # 높이 3
    elif high == 3:
        alist = []
        count = 0
        while count < 7:
            a = random.randint(1, 9)
            if a not in alist:
                alist.append(a)
                count += 1
            
        print(f"{" "}{" "}{alist[0]}")
        print(f"{" "}{alist[1]}{alist[2]}")
        print(f"{alist[3]}{alist[4]}{alist[5]}")
                        
menu()