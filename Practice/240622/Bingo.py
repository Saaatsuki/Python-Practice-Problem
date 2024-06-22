import random

bingo25 = list(range(1, 26))
bingo5X5 = []

# ビンゴカード生成
for count in range(5):
    bingo5 = random.sample(bingo25, 5) 
    bingo5X5.append(bingo5)
    for num in bingo5:
        bingo25.remove(num)
    print(" ".join(f"{num:02d}" for num in bingo5))

game_count = 0
bingo_count_all = 0

while bingo_count_all < 3: 
    game_count += 1
    bingo_count_reset = 0

    user_num = int(input(f"{game_count}번째: 숫자를 입력하세요: "))
    while not 1 <= user_num <= 25:
        user_num = int(input(f"{game_count}번째: 1에서 25 사이의 숫자를 입력하세요: "))

    found = False
    for list_idx in range(5):
        if user_num in bingo5X5[list_idx]:
            num_idx = bingo5X5[list_idx].index(user_num)
            bingo5X5[list_idx][num_idx] = 0
            found = True
            break

    for list_idx in range(5):
        if all(num == 0 for num in bingo5X5[list_idx]):
            bingo_count_reset += 1

    for num_idx in range(5):
        if all(bingo5X5[list_idx][num_idx] == 0 for list_idx in range(5)):
            bingo_count_reset += 1

    if all(bingo5X5[i][i] == 0 for i in range(5)):
        bingo_count_reset += 1

    if all(bingo5X5[i][4-i] == 0 for i in range(5)):
        bingo_count_reset += 1

    if bingo_count_reset > bingo_count_all:
        print("BINGOOO!!")

    bingo_count_all = bingo_count_reset
    print(f"현재까지의 빙고 : {bingo_count_all}")

print(f"\n3개 빙고!! 시도 횟수 : {game_count}")
