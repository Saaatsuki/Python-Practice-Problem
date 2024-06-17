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
bingo_count_all = 0
user_num_li = []

while bingo_count_all < 3:
    game_count += 1
    bingo_count_reset = 0
    
    user_num = int(input(f"{game_count}시도 - 숫자를 입력 해 주세요 : "))
    while not (1 <= user_num <= 25) and user_num in user_num_li:
        if 1 <= user_num <= 25 :
            user_num = int(input("1에서 25 사이의 숫자를 입력하세요 : "))
        else:
            user_num = int(input("이미 입력한 숫자입니다. 다른 숫자를 입력하세요 :"))
    user_num_li.append(user_num)  # appendで修正

    print("숫자를 확인합니다!!")

    bingo_count_reset = 0

    # 横のチェック（行ごとにチェック）
    for line in bingo_all_li:  # 横
        # if all(num in user_num_li for num in line)
        #   bingo_count_reset += 1
        line_all_in_user_num_li = True
        for num in line:
            if num not in user_num_li:
                line_all_in_user_num_li = False
                break
        if line_all_in_user_num_li:
            bingo_count_reset += 1

    # 縦のチェック（列ごとにチェック）
    for col in range(5):  # 縦
        # if all(bingo_all_li[line][col] in user_num_li for row in range(5))
        #   bingo_count_reset += 1
        col_all_in_user_num_li = True
        for line in range(5):# line:横(行)　col:縦(列)
            if bingo_all_li[line][col] not in user_num_li:
                col_all_in_user_num_li = False
                break
        if col_all_in_user_num_li:
            bingo_count_reset += 1

    # 斜めのチェック（メイン対角線）
    # if all(bingo_all_li[i][i] in user_num_li for i in range(5))
    #   bingo_count_reset += 1
    main_diagonal_all_in_user_num_li = True
    for i in range(5):  # 斜め＼
        if bingo_all_li[i][i] not in user_num_li:
            main_diagonal_all_in_user_num_li = False
            break
    if main_diagonal_all_in_user_num_li:
        bingo_count_reset += 1

    # 斜めのチェック（逆対角線）
    # if all(bingo_all_li[i][4 - i] in user_num_li for i in range(5))
    #   bingo_count_reset += 1
    anti_diagonal_all_in_user_num_li = True
    for i in range(5):  # 斜め／
        if bingo_all_li[i][4 - i] not in user_num_li:
            anti_diagonal_all_in_user_num_li = False
            break
    if anti_diagonal_all_in_user_num_li:
        bingo_count_reset += 1

    if bingo_count_reset > bingo_count_all:
        print("BINGOOO!!")
    bingo_count_all = bingo_count_reset
    print(f"현재까지의 빙고 : {bingo_count_all}")
    
print(f"\n3개 빙고!! 시도 횟수 : {game_count}")