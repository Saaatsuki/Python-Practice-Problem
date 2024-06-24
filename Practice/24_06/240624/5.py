def getSplit(argList,argSep):
    word_li = []
    word = ""
    for char in argList:
        if char != argSep:
            word += char
        else:
            if word:
                word_li.append(word)
                word = ""
    if word:
        word_li.append(word)
    return word_li


def getJoin(argList,argSep):
    index = 0
    result = ""
    while index<len(argList):
        result += str(argList[index])
        index += 1
        if index<len(argList):
            result += argSep
    return result

print(getJoin([10,20,30,40,50,60,70,80,],"💛"))


def getJoin(argList,argSep):
    result = ""
    index = 0
    while index<len(argList):
        result += argList[index]
        index += 1
        if index<len(argList):
            result += argSep
    return result