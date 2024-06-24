import random

bingo25_li_1_9 = ["01","02","03","04","05","06","07","08","09"]
bingo25_li_10_25 = [str(i) for i in range(10,26)]
bingo25_li_num = bingo25_li_1_9 + bingo25_li_10_25



bingo25_li = bingo25_li_num[:]
bingo_all_li = []
for i in range(5):
    bingo_order_li = random.sample(bingo25_li_num, 5)
    bingo_all_li.append(bingo_order_li)
    for num in bingo_order_li:
        bingo25_li_num.remove(num)
    print(" ".join(bingo_order_li))

bingo_li_1 = bingo_all_li[0]
bingo_li_2 = bingo_all_li[1]
bingo_li_3 = bingo_all_li[2]
bingo_li_4 = bingo_all_li[3]
bingo_li_5 = bingo_all_li[4]

game_count = 0
bingo_count = 0
user_num_li = []

while bingo_count < 3:
    game_count += 1
    user_num = input(f"{game_count}시도 - 숫자를 입력 해 주세요 : ")
    while user_num not in bingo25_li:
        user_num = input("01 에서 25 사이의 숫자를 입력 해 주세요 : ")

    user_num_li.append(user_num)
    print("숫자를 확인합니다!!")

    bingo_tf = False

    # 横のビンゴチェック
    for line in bingo_all_li:
        if all(num in user_num_li for num in line):
            bingo_tf = True

    # 縦のビンゴチェック
    for col in range(5):
        if all(bingo_all_li[row][col] in user_num_li for row in range(5)):
            bingo_tf = True

    # 斜めのビンゴチェック（左上から右下）
    if all(bingo_all_li[i][i] in user_num_li for i in range(5)):
        bingo_tf = True

    # 斜めのビンゴチェック（右上から左下）
    if all(bingo_all_li[i][4-i] in user_num_li for i in range(5)):
        bingo_tf = True

    if bingo_tf:
        bingo_count += 1
        print("BINGOOO!!")
    print(f"현재까지의 빙고 : {bingo_count}")

print(f"3개 빙고!! 시도 횟수 : {game_count}")