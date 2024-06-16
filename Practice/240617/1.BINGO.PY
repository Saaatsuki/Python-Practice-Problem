import random

bingo25_li = [i for i in range(1, 26)]
bingo25_li_none = bingo25_li[:]
bingo_all_li = []
for _ in range(5):
    bingo_order_li = random.sample(bingo25_li_none, 5)
    bingo_all_li.append(bingo_order_li)    
    for j in bingo_order_li:
        bingo25_li_none.remove(j)
    bingo5X5 = " ".join("{:02}".format(num) for num in bingo_order_li)
    print(bingo5X5)

game_count = 0
bingo_count = 0
user_num_li = []

while bingo_count < 3:
    game_count += 1
    bingo_count = 0
    
    user_num = int(input(f"{game_count}시도 - 숫자를 입력 해 주세요 : "))
    while not (1 <= user_num <= 25):
        user_num = int(input("1에서 25 사이의 숫자를 입력하세요: "))

    user_num_li.append(user_num)  # appendで修正

    print("숫자를 확인합니다!!")

    bingo_tf = False
    for line in bingo_all_li:  # 横
        if all(num in user_num_li for num in line):
            bingo_tf = True
    for col in range(5):  # 縦
        if all(bingo_all_li[row][col] in user_num_li for row in range(5)):
            bingo_tf = True
    if all(bingo_all_li[i][i] in user_num_li for i in range(5)):  # 斜め＼
        bingo_tf = True
    if all(bingo_all_li[i][4 - i] in user_num_li for i in range(5)):  # 斜め／
        bingo_tf = True
    if bingo_tf:
        bingo_count += 1
        print("BINGOOO!!")
    print(f"현재까지의 빙고 : {bingo_count}")

print(f"3개 빙고!! 시도 횟수 : {game_count}")
