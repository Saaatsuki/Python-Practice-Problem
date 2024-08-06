while True:
    print("-"*30)
    print("1) 구구단 출력")
    print("2) 랜덤값 삼각형 출력")
    print("3) 중료")
    print("-"*30)

    menu = int(input("원하는 메뉴 번호를 입력하세요 : "))
    while not 1<=menu<=3:
        menu = int(input("1~3사이의 값을 입력하세요 :"))

        if menu == 1:
            gugu_input = input()
            if "~" in gugu_input:
                start, end = map(int,gugu_input.split("~"))
                gugu_li = list(range(start, end + 1))
            else:
                gugu_li = list(map(int,gugu_input.split(",")))
            
            if all(2 <= num <= 9 for num in gugu_li):
                for num1 in gugu_li:
                    print(f"구구 {num1}단 ")
                    for num2 in range(1,10):
                        print(f"{num1} X {num2} = {num1 * num2}")
                    print()
                break
            else:
                print("1~9의 숫자를 입력하세요.")
        
        elif menu == 2:
            pass
        elif menu == 3:
            print("")