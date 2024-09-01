import random

def randomSample(argList, argK):
    if len(argList) < argK:
        raise ValueError("argListの長さがargKより小さいです")
    sample = []
    argList_copy = argList[:]
    for _ in range(argK):
        index = random.randint(0, len(argList_copy) - 1)
        sample.append(argList_copy.pop(index))
    return sample

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

def getJoin(argList, argSep):
    join = ""
    index = 0
    while index < len(argList):
        join += argList[index]
        index += 1
        if index < len(argList):
            join += argSep
    return join

def getIn(argBig, argSmall):
    for val in argBig:
        if val == argSmall:
            return True
    return False

while True:
    print("-" * 20)
    print("1）九九の段")
    print("2）数字ピラミット")
    print("3）終了")
    print("-" * 20)

    menu = int(input("メニュー番号を選んでください："))

    if menu == 1:
        while True:
            gugu = input("出力したい九九の段を入力してください。")
            if getIn(gugu, "~"):
                split_li = getSplit(gugu, "~")
                gugu_li = [int(num) for num in range(int(split_li[0]), int(split_li[1]) + 1)]
            else:
                split_li = getSplit(gugu, ",")
                gugu_li = [int(num) for num in split_li]
            if all(2 <= num <= 9 for num in gugu_li):
                for num1 in gugu_li:
                    print()
                    for num2 in range(1, 10):
                        print(f"{num1} X {num2} = {num1 * num2:02d}")
                break
            else:
                print("2~9の数字を入力してください")

    elif menu == 2:
        while True:
            high = int(input("何段の数字ピラミットにしますか："))
            numK = high * (high + 1) // 2
            if numK > 9:
                print("最大で9つの数字しかありません。もう一度試してください。")
                continue
            li1 = randomSample([num for num in range(1, 10)], numK)
            index = 0
            for i in range(1, high + 1):
                li2 = li1[index:index + i]
                txt = getJoin([f"{num}" for num in li2], "")
                print(f'{" " * (high - i)}{txt}')
                index += i
            break

    elif menu == 3:
        print("プログラムを終了します")
        break

    else:
        print("1~3のメニュー番号を選んでください")
