import random

target_list = [i for i in range(1, 26)]
number_list = []
for i in range(25):
    number_list.append(target_list.pop(random.randint(0, len(target_list) - 1)))

bingo_field = [[number_list[i + j] for i in range(5)] for j in range(0, 25, 5)]

for line in bingo_field:
    print(" ".join(map(str, line)))

print()

current_bingo = 0
bingo = 0
count = 0
while bingo < 3:
    bingo = 0
    count += 1
    num = int(input(f"{count}번째 시도 - 숫자를 입력 해 주세요: "))
    while not (num > 0 and num < 26):
        num = int(input("1 에서 25 사이의 숫자를 입력 해 주세요: "))
    
    isExist = False
    for i in range(5):
        for j in range(5):
            if bingo_field[i][j] == num:
                isExist = True
                bingo_field[i][j] = 0
                break
        if isExist:
            break

    if isExist:
        print("숫자를 체크했습니다!")
    else:
        print("이미 체크 된 숫자입니다.")

    # 가로 체크
    for i in range(5):
        isBingo = True
        for j in range(5):
            if bingo_field[i][j] != 0:
                isBingo = False
                break
        if isBingo:
            bingo += 1

    # 세로 체크
    for i in range(5):
        isBingo = True
        for j in range(5):
            if bingo_field[j][i] != 0:
                isBingo = False
                break
        if isBingo:
            bingo += 1

    # 대각선 체크
    isBingo = True
    for i in range(5):
        if bingo_field[i][i] != 0:
            isBingo = False
            break
    
    if isBingo:
        bingo += 1

    isBingo = True
    for i in range(5):
        if bingo_field[4 - i][i] != 0:
            isBingo = False
            break
    if isBingo:
        bingo += 1
    
    if bingo > current_bingo:
        print("BINGO!!!!!!!!")
        current_bingo = bingo
    print(f"현재까지의 빙고: {bingo}\n")

print(f"{bingo}개 빙고!! 시도 횟수 {count}")