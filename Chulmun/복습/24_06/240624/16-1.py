import random

def randomSample(argList, argK):
    if len(argList) < argK:
        raise ValueError("リストの長さがサンプル数よりも少ないです")
    
    sample = []
    argList_copy = argList.copy()
    for _ in range(argK):  # argK回のループを行う
        index = random.randint(0, len(argList_copy) - 1)
        sample.append(argList_copy.pop(index))
    return sample

def getIn(argBig, argSmall):
    for val in argBig:
        if val == argSmall:
            return True
    return False

def getJoin(argList, argSep):
    result = ""
    index = 0
    while index < len(argList):  # index < len(argList) でループするよう修正
        result += str(argList[index])
        index += 1
        if index < len(argList):
            result += argSep
    return result

def getSplit(argTxt, argSep):
    word = ""
    word_li = []
    for char in argTxt:
        if char != argSep:
            word += char
        else:
            if word:
                word_li.append(word)
                word = ""
    if word:
        word_li.append(word)
    return word_li

com_num_li = randomSample([num for num in range()], 3)

game_count = 0
strike = 0
ball = 0
out = 0

while game_count < 5 and strike < 3 and out < 3:
    game_count += 1
    user_txt = input(f"{game_count}回目：入力した数字をスペースで区切って入力してください：")
    user_num_li = [int(val) for val in getSplit(user_txt, " ")]

    strike = 0
    ball = 0

    for i in range(len(com_num_li)):
        if com_num_li[i] == user_num_li[i]:
            strike += 1
        elif getIn(com_num_li, user_num_li[i]):
            ball += 1

    if strike == 0 and ball == 0:
        out += 1

    print(f"結果：{strike} Strike, {ball} Ball, {out} Out")

print("ゲーム終了")
