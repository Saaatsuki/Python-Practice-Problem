# 구구단 작성

while True:
    print("-"*20)
    print("1,구구단 출력")
    print("2,프로그램 종료")
    print("-"*20)
    
    cho = int(input())
    
    if (cho == 1):
        number = int(input("출력할 구구단의 단을 입력하세요,구구단의 2-9 사이 입력\n"))
        while True:
            if (1 < number < 10):
                for i in range (2,10):
                    answer =number * int(i)
                    print(str(number),"×",str(i),"=",answer)
                    break
            else:
                number = int(input("2-9사이 정수를 입력하세요"))
            
    elif (cho == 2):
        print("이용 해주셔서 감사합니다.")
        break
    
    else:
        print("잘못 입력하셨습니다. 다시 입력하세요.")       
    
        