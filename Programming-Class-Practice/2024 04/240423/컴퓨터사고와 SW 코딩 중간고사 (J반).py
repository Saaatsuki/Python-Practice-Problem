print("--------------------------")
print("1, 홀수 짝수 구분 프로그램")
print("2, 3의 배수 확인 프로그램")
print("--------------------------")

menu = int(input("메뉴를 선택해 주십시오.\n"))

   

if (menu == 1):
    print("홀수 짝수 구분 프로그램을 선택 하셨습니다")
    number = int(input("정수 값을 입력 하세요.\n"))
    if (number %2==0):
        print("입력 하신 값",number,"짝수입니다.")
    else:
        print("입력 하신 값",number,"홀수입니다.")

elif (menu == 2):
    print("3의 배수 학인 프로그램을 선텍 하셨습니다. ")
    number = int(input("정수 값을 입력 하세요.\n"))
    if(number == 3):
        print("입력 하신 값 3은 유효하지 않은 메뉴 선텍 값입니다.메뉴 선택은 1과 2만 가능합니다.")
    elif (number %3==0):
        print("입력 하신 값",number,"3의 배수입니다.")
    else:
        print("입력 하신 값",number,"3의 배수아닙니다.")    