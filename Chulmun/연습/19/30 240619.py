import random

menu_num = 0
while menu_num != 3:
    menu_num = int(input("------------------\n1.구구단 출력\n2.랜덤값 삼각형 출력\n3.종료\n------------------\n원하는 메뉴 번호를 입력하세요 : "))
    while not 1 <= menu_num <= 3:
        menu_num = int(input("1 or 2 or 3 부터 선택해주세요\n------------------\n1.구구단 출력\n2.랜덤값 삼각형 출력\n3.종료\n------------------\n원하는 메뉴 번호를 입력하세요 : "))
    if menu_num == 1:
        in29_tf = False
        while not in29_tf:
            gugu_user = input(f"출력할 구구단을 아래 형식으로 입력하세요 (에:2,2~5)\n")
            gugu_error_msg = f"2~9사이의 값을 입력하세요"
            if "~" in gugu_user:
                argNum = list(map(int, gugu_user.split("~")))
                if len(argNum) == 2 and 2 <= argNum[0] <= 9 and 2 <= argNum[1] <= 9 and argNum[0] <= argNum[1]:
                    for i in range(argNum[0], argNum[1] + 1):
                        print()
                        for j in range(1, 10):
                            print(f"{i} X {j} = {i*j}")
                    in29_tf = True
                else:
                    print(gugu_error_msg)
            else:
                gugu_num = int(gugu_user)
                if 2 <= gugu_num <= 9:
                    for i in range(1, 10):                
                        print(f"{gugu_num} X {i} = {gugu_num * i}")
                    in29_tf = True
                else:
                    print(gugu_error_msg)

    elif menu_num == 2:
        tri_user = int(input(f"삼각형의 높이 줄 수를 입력하세요 (2 또는 3): "))
        while not 2 <= tri_user <= 3:
            tri_user = int(input(f"2 또는 3를 입력하세요: "))

        tri_com_li = []
        required_length = 3 if tri_user == 2 else 6
        while len(tri_com_li) < required_length:
            com_num = random.randint(0, 9)
            if com_num not in tri_com_li:
                tri_com_li.append(com_num)
        # if tri_user == 2:
        #     print(f" {tri_com_li[0]}\n{tri_com_li[1]}{tri_com_li[2]}")
        # else:
        #     print(f"  {tri_com_li[0]}\n {tri_com_li[1]}{tri_com_li[2]}\n{tri_com_li[3]}{tri_com_li[4]}{tri_com_li[5]}")
        index = 0
        for i in range(1, tri_user + 1):
            print(" " * (tri_user - i) + "".join(map(str, tri_com_li[index:index + i])))
            index += i
    
    else:
        print("프로그램을 종료합니다.")