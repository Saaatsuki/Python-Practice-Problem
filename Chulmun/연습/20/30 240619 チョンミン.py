import random

# 1. 메뉴 출력
def print_menu():
    print("------------")
    print("1. 구구단 출력")
    print("2. 랜덤값 삼각형 출력")
    print("3. 종료")
    print("------------")

# 2. 메뉴 선택 후 해당 함수 호출
def menu_choice():
    while True : # 올바른 입력까지 반복
        print_menu() # 2-1. 메뉴창 호출
        menu = int(input("원하는 메뉴를 입력하세요: ")) # 메뉴 선택

        if menu < 0 or menu > 3 : # 올바른 범위 벗어날 시 계속 반복
            print("1~3 중에서 선택하세요")
                   
        elif menu == 1 : # 구구단 호츌
            multiplication_table()
        
        elif menu == 2 : # 삼각형 호출
            Triangle_table()
        
        elif menu == 3 : # 프로그램 종료
            print("프로그램을 종료합니다")
            break
    
# 3. 구구단 함수   
def multiplication_table():
        while True: #잘못된 입력시 반복
            
            num = list(input("출력 할 구구단을 아래 형식으로 입력하세요(예 : 2, 2~5):"))
            
            if len(num) > 1 : # 리스트의 길이가 2 이상일때
                num.remove("~") # "~" 삭제

                # 구구단 범위를 벗어나면 재입력
                if int(num[0]) < 2 or int(num[0]) > 9 or int(num[1]) < 2 or int(num[1]) > 9:
                    print("2~9 사이 수를 입력하세요")

                # 범위가 올바를 때
                else:
                    for i in range(int(num[0]),(int(num[1]) + 1)): # 구구단 출력
                        for j in range(1,10):
                            print(f"{i}*{j}={i*j}")
                        print() # 줄바꿈
                    break  # 루프 종료
            else :
                if int(num[0]) < 2 or int(num[0]) > 9 : # 범위를 벗어나면 다시 입력 요청
                    print("2~9 사이 수를 입력하세요")

                else: 
                    num = int(num[0]) # 숫자 하나만 입력 시
                    for k in range(1,10): #구구단 출력
                        print(f"{num} * {k} = {num*k}")                
                    break  # 루프 종료

#4. 삼각형 함수
def Triangle_table():
    while True:
        Height = int(input("삼각형의 높이 줄 수를 입력하세요(2 이상 3이하)"))
        if Height == 2 : #높이가 2일때
            num_list=[i for i in range(1,10)] #1~9까지만 뽑기  
            one_choice = random.choice(num_list) #랜덤 뽑기
            print("",one_choice) # 제일 윗줄
            num_list.remove(one_choice) # 반복 방지위해 삭제
    
            for _ in range(2): # 두번째 줄 2개 뽑기
                two_choice = random.choice(num_list)
                num_list.remove(two_choice) #반복 방지 위해 삭제
                print(two_choice,end="") # 한줄 출력
            print() #줄바꿈
            break  #루프 종료
        
        elif Height == 3 : #높이가 3일때
            num_list=[i for i in range(1,10)] #1~9까지만 뽑기    
            one_choice = random.choice(num_list) #랜덤 뽑기
            print(" ",one_choice) # 제일 윗줄
            num_list.remove(one_choice) #반복 방지

            print(" ",end="") # 두번째 줄 한칸 띄우기
            
            for _ in range(2): #두번째 줄 
                two_choice = random.choice(num_list) #랜덤 뽑기
                print(two_choice,end="") # 한줄 출력
                num_list.remove(two_choice) #반복 방지
            print() # 줄바꿈

            for _ in range(3): # 마지막 줄
                three_choice = random.choice(num_list) #랜덤 뽑기
                num_list.remove(three_choice) # 반복 방지
                print(three_choice,end="")  # 한줄 출력
            print() #줄바꿈
            break  # 루프 종료
        
        else:
            print("2~3 사이의 숫자를 입력하세요") # 잘못된 입력시 재입력


menu_choice()