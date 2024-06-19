import random

li = [[],[],[],[],[]]
# 5번 2차원 리스트에 삽입
for i in range(5):
    count = 5 # 원소는 5개임
    while count > 0:
        # 랜덤으로 숫자를 선택
        random_num = random.randint(1,25)
        flag = True
        for j in li:
            for l in j: # 리스트를 돌려서 중복을 확인
                if l == random_num :
                    flag = False
                    break
        if flag:
            li[i].append(random_num)
            count -= 1
# bingo를 출력
for lists in li:
    print(*lists)

game_count = 0
Bingo_count = 0
# 게임 시작
while Bingo_count < 3:
    bingo = Bingo_count
    Bingo_count = 0
    game_count += 1
    
    # 숫자를 입력 받기
    msg = (f"{game_count}번째 시도 - 숫자를 입력해주세요 : ")
    while True:
        input_num = int(input(msg))
        if 1 <= input_num <= 25:
            break
        else:
            msg = "1 에서 25 사이의 숫자를 입력해주세요 : "
    # 숫자를 체크해서 0으로 바꾸기
    for i in range(5):
        for j in range(5):
            if li[i][j] == input_num :
                li[i][j] = 0
                print("숫자를 체크 했습니다!")
    
    count_r = 0# naname ->
    count_l = 0  # naname <-
    # 1index, 2index를 돌려서 체크
    for i in range(5):
        count_x = 0
        
        count_y = 0
        for j in range(5):
            # 세로 5개 다 0이면 bingo
            if li[j][i] == 0:
                count_y += 1 
                if count_y >= 5:
                    Bingo_count += 1
            # 가로 5개 다 0이면 bingo
            if li[i][j] == 0:
                count_x += 1 
                if count_x >= 5:
                    Bingo_count += 1
        # 같은 index면 naname ->
        if li[i][i] == 0 :
            count_r += 1
        # 반대 index면 naname <-
        if li[i][4 - i] == 0:
            count_l += 1
    # 같은 index가 5개
    if count_r == 5:
        Bingo_count += 1
    # 반대 index가 5개
    if count_l == 5:
        Bingo_count += 1
    # 전에 출력했을 때 보다 증가하면 출력
    if bingo < Bingo_count:
        print("BINGO!!!!!!")
    # 결과 출력
    print(f"현재까지의 빙고: {Bingo_count}\n")
print(f"{Bingo_count}개 빙고!! 시도 횟수 {game_count}")