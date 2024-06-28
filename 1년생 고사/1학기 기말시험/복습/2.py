import random

def sampleRandom(argList, argK):
    if len(argList) < argK:
        raise ValueError("List size is smaller than the sample size")
    sample = []
    argList_copy = argList[:]
    for _ in range(argK):
        index = random.randint(0, len(argList_copy) - 1)
        sample.append(argList_copy.pop(index))
    return sample

def getIn(argBig,argSmall):
    for i in argBig:
        if i == argSmall:
            return True
    return False

def getJoin(argList,argSep):
    join = ""
    index = 0
    while index<len(argList):
        join += str(argList[index])
        index += 1
        if index<len(argList):
            join += argSep
    return join

def getAll(iterable):
    for elem in iterable:
        if not elem:
            return False
    return True

def checkBingo(board, size):
    bingo_count = 0
    # 縦
    for i in range(size):
        if getAll(x == '*' for x in board[i * size:(i + 1) * size]):
            bingo_count += 1
    # 横
    for i in range(size):
        if getAll(board[j * size + i] == '*' for j in range(size)):
            bingo_count += 1
    # 斜め＼
    if getAll(board[i * size + i] == '*' for i in range(size)):
        bingo_count += 1
    # 斜め／
    if getAll(board[i * size + (size - 1 - i)] == '*' for i in range(size)):
        bingo_count += 1
    return bingo_count


tate_yoko = int(input("何段のビンゴゲームを始めますか："))
while not 3<=tate_yoko<=6:
    tate_yoko = int(input("3～6段にしてください。何段のビンゴゲームを始めますか："))

tate_yoko_count = tate_yoko * tate_yoko

bingo_num_li = sampleRandom([num for num in range(1, 37)], tate_yoko_count)

index = 0
for _ in range(tate_yoko):
    li1 = bingo_num_li[index:index+(tate_yoko)]
    li2 = [f"{num:2d}" for num in li1]
    print(getJoin(li2, " "))
    index += tate_yoko

bingo_count = 0
game_count = 0

while True:
    game_count += 1
    user_num = int(input(f"{game_count}回目：ビンゴナンバーを入力してください："))
    while not getIn(bingo_num_li, user_num):
        user_num = int(input(f"{game_count}回目：このナンバーはボードにありません。\nもう一度ビンゴナンバーを入力してください："))

    # 入力された数字は"*"に変換
    for index in range(len(bingo_num_li)):
        if bingo_num_li[index] == user_num:
            bingo_num_li[index] = '*'

    index = 0
    for _ in range(tate_yoko):
        li1 = bingo_num_li[index:index + tate_yoko]
        li2 = [f"{str(num):2s}" for num in li1]
        print(getJoin(li2, " "))
        index += tate_yoko
    
    bingo_lines = checkBingo(bingo_num_li, tate_yoko)
    if bingo_lines >= 2:
        break

print("おめでとうございます！！あなたは2つ以上のビンゴしました！！")