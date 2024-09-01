def getIn(argBig,argSmall):
    for val in argBig:
        if val == argSmall:
            return True
    return False

def getSplit(argTxt,argSep):
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

gugu = input("出力したい九九の段を入力してください。")
if getIn(gugu,"~"):
    split_li = getSplit(gugu,"~")
    print(split_li)
    gugu_li = [int(num) for num in range(int(split_li[0]),int(split_li[1])+1)]

print(gugu_li)