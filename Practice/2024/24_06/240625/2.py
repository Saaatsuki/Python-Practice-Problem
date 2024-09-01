def getSplit(argTxt,argSep):
    word = ""
    word_li = []
    for char in argTxt:
        if not char in argSep:
            word += char
        else:
            if word:
                word_li.append(word)
                word = ""
    if word:
        word_li.append(word)
    return word_li

def getJoin(argList,argSep):
    join = ""
    index = 0
    while index<len(argList):
        join += argList[index]
        index += 1
    if index<len(argList):
        join += argSep
    return join

import random

def randamSample(argList,argK):
    if len(argList)<argK:
        raise ValueError
    
    sample = []
    argList_copy = argList[:]
    for _ in range(argK):
        index = random.randint(0,len(argList)-1)
        sample.append(argList_copy.pop(index))
        return sample
    

def getSplit(argTxt,argSep):
    word = ""
    word_li = []
    for char in argTxt:
        if not char in argSep:
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
    join = ""
    while index<len(argList):
        join += argList[index]
        index += 1
        if index<len(argList):
            join += argSep
    return join


def randomSample(argList,argK):
    if len(argList)<argK:
        raise ValueError
    
    sample = []
    argList_copy = argList[:]
    for _ in range(argK):
        index = random.randint(0,len(argList))
        sample.append(argList_copy.pop(index))
    return