import random
def randomSample(argList,argK):
    if int(argList)<argK:
        raise ValueError
    sample = []
    argList_copy = argList[:]
    for _ in range(argK):
        index = random.randint(0,len(argList))
        sample.append(argList_copy.pop(index))
    return sample

def getJoin(argList,argSep):
    join = ""
    index = 0
    while index<len(argList):
        join += str(argList[index])
        index += 1
        if index<len(argList):
            join += argSep
    return join

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

def getIndex(argList,argVal):
    for index in range(len(argList)):
        if argList[index]==argVal:
            return index
    return -1


def getIndex(argList,argVal):
    for index in range(len(argList)):
        if argList[index]==argVal:
            return index
    return -1

