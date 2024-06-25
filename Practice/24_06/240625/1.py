def getSplit1(argTxt,argSep):
    word_li = []
    word = ""
    for char in argTxt:
        if char != argSep:
            word += char
        else:
            if word:
                word_li.append(word)
                word = ""
    if word:
        word_li.append(word)

def getJoin(argList,argSep):
    join_result = ""
    index = 0
    while index<len(argList):
        join_result += argList[index]
        index += 1
        if index<len(argList):
            join_result += argSep
    return join_result

import random

def randomSample(argList,argK):
    if len(argList)<argK:
        raise ValueError("エラー")
    
    sample = []
    argList_copy = argList[:]
    for _ in range(argK):
        index = random.randint(0,len(argList_copy)-1)
        sample.append(argList_copy.pop(index))
    return sample

def randomSample(argList,argK):
    if len(argList)<argK:
        raise ValueError
    sample = []
    argList_copy = argList[:]
    for _ in range(argK):
        index = random.randint(0,len(argList_copy))
        sample.append(argList_copy.pop(index))
    return sample

def getJoin(argTxt,argSep):
    join = ""
    index = 0
    while index<len(argTxt):
        join += argTxt[index]
        index += 1
        if index<len(argTxt):
            join += argSep
    return join
    
def getJoin(argTxt,argSep):
    index = 0
    join = ""
    while index<len(argTxt):
        join += argTxt[index]
        index += 1
        if index<len(argTxt):
            join += argSep
    return join

def randomSanple(argList,argK):
    if len(argList)<argK:
        raise ValueError
    
    sample = []
    argList_list = argList[:]
    for _ in range(argK):
        index = random.randint(0,len(argList)-1)
        sample.append(argList_list.pop(index))


        