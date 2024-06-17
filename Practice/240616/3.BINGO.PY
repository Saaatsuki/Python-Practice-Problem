import random

# ビンゴフィールドの初期化
target_list = [i for i in range(1, 26)]
random.shuffle(target_list)

bingo_field = [[target_list[i + j] for i in range(5)] for j in range(0, 25, 5)]

def print_bingo_field(field):
    for line in field:
        print(" ".join(f"{num:02}" for num in line))
    print()

print_bingo_field(bingo_field)

# ゲーム状態の初期化
current_bingo = 0
bingo = 0
count = 0
checked_numbers = []

def check_bingo(field):
    bingo = 0
    # 横のビンゴチェック
    for row in field:
        if all(num == 0 for num in row):
            bingo += 1

    # 縦のビンゴチェック
    for col in range(5):
        if all(field[row][col] == 0 for row in range(5)):
            bingo += 1

    # 斜めのビンゴチェック
    if all(field[i][i] == 0 for i in range(5)):
        bingo += 1
    if all(field[i][4 - i] == 0 for i in range(5)):
        bingo += 1

    return bingo

while bingo < 3:
    count += 1
    num = int(input(f"{count}번째 시도 - 숫자를 입력 해 주세요: "))
    while not (1 <= num <= 25):
        num = int(input("1 에서 25 사이의 숫자를 입력 해 주세요: "))
    while num in checked_numbers:
        num = int(input("이미 체크 된 숫자입니다. 다른 숫자를 입력 해 주세요: "))

    checked_numbers.append(num)

    isExist = False
    for i in range(5):
        for j in range(5):
            if bingo_field[i][j] == num:
                bingo_field[i][j] = 0
                isExist = True
                break
        if isExist:
            break

    if isExist:
        print("숫자를 체크했습니다!")
    else:
        print("이미 체크 된 숫자입니다.")

    bingo = check_bingo(bingo_field)

    if bingo > current_bingo:
        print("BINGO!!!!!!!!")
        current_bingo = bingo

    print_bingo_field(bingo_field)
    print(f"현재까지의 빙고: {bingo}\n")

print(f"{bingo}개 빙고!! 시도 횟수 {count}")