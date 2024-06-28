import random

def randomSample(argList, argK):
    if len(argList) < argK:
        raise ValueError("Sample size cannot be larger than the list size")
    sample = []
    argList_copy = argList[:]
    for _ in range(argK):
        index = random.randint(0, len(argList_copy) - 1)
        sample.append(argList_copy.pop(index))
    return sample

def getJoin(argList, argSep):
    return argSep.join(f"{num:02d}" if isinstance(num, int) else "*" for num in argList)

def getIn(argBig, argSmall):
    return argSmall in argBig

def getCount(argList, argVal):
    return argList.count(argVal)

# ユーザーからNXNのNの値を受け取る
numD = int(input("Enter the size of the bingo board (3 to 6): "))
while not 3 <= numD <= 6:
    numD = int(input("Size must be between 3 and 6. Please try again.\nEnter the size of the bingo board (3 to 6): "))

numDXnumD = numD * numD

# ランダムな数字を生成
diceNXN = random.sample(range(1, 37), numDXnumD)

dice_N_all = [diceNXN[i*numD:(i+1)*numD] for i in range(numD)]
print("Initial Bingo Board:")
for row in dice_N_all:
    print(getJoin(row, " "))

game_count = 0
bingo_count = 0

# コピーを作成
dice_N_all_copy = [row[:] for row in dice_N_all]

def check_bingo(board):
    bingo_count = 0
    # 横
    for row in board:
        if all(cell == "*" for cell in row):
            bingo_count += 1
    
    # 縦
    for col in range(numD):
        if all(board[row][col] == "*" for row in range(numD)):
            bingo_count += 1

    # 斜め（＼）
    if all(board[i][i] == "*" for i in range(numD)):
        bingo_count += 1
    
    # 斜め（／）
    if all(board[i][numD - i - 1] == "*" for i in range(numD)):
        bingo_count += 1
    
    return bingo_count

while bingo_count < 2:
    game_count += 1

    user_num = int(input(f"Enter a number (1-36) for round {game_count}: "))

    for row in dice_N_all_copy:
        for col in range(len(row)):
            if row[col] == user_num:
                row[col] = "* "
    
    bingo_count = check_bingo(dice_N_all_copy)

    print(f"Board after round {game_count}:")
    for row in dice_N_all_copy:
        print(getJoin(row, " "))

print("Congratulations!! You've won the game with 2 or more bingos!")
