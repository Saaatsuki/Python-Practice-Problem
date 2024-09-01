import random

def check_bingo(board, size):

    bingo_count = 0

    # 縦
    for i in range(size):
        if all(board[i * size + j] == '*' for j in range(size)):
            bingo_count += 1
    
    # 横
    for i in range(size):
        if all(board[j * size + i] == '*' for j in range(size)):
            bingo_count += 1
    
    # 斜め＼
    if all(board[i * size + i] == '*' for i in range(size)):
        bingo_count += 1
    
    # 斜め／
    if all(board[i * size + (size - 1 - i)] == '*' for i in range(size)):
        bingo_count += 1
    
    return bingo_count

def display_board(board, size):
    for i in range(size):
        print(" ".join(f"{str(board[i * size + j]):2s}" for j in range(size)))

# ビンゴゲームのサイズを決定
while True:
    tate_yoko = int(input("何段のビンゴゲームを始めますか："))
    if 3 <= tate_yoko <= 6:
        break
    print("3～6段にしてください。")

board_size = tate_yoko * tate_yoko
bingo_numbers = random.sample([num for num in range(1, 37)], board_size)

# 初期ビンゴボードを表示
display_board(bingo_numbers, tate_yoko)

game_count = 0

# ゲームループ
while True:
    game_count += 1
    user_num = int(input(f"{game_count}回目：ビンゴナンバーを入力してください："))
    
    while user_num not in bingo_numbers:
        user_num = int(input(f"{game_count}回目：このナンバーはボードにありません。\nもう一度ビンゴナンバーを入力してください："))

    # 入力された数字を"*"に変換
    bingo_numbers = ['*' if num == user_num else num for num in bingo_numbers]

    # ビンゴボードを表示
    display_board(bingo_numbers, tate_yoko)
    
    # ビンゴラインのチェック
    if check_bingo(bingo_numbers, tate_yoko) >= 2:
        break

print("おめでとうございます！！あなたは2つ以上のビンゴしました！！")