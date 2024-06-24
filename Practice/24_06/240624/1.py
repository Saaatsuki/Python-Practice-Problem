def getSplit1(argSentence,argSplit):
    word_li = []
    word = ""

    for char in argSentence:
        if char != argSplit:
            word += char
        else:
            if word:
                word_li.append(word)
                word = ""
    else:
        if word:
            word_li.append(word)
    return word_li


sentence1 = "hello he hehe hellos hellllo helowww hello hello hello"
print(getSplit1(sentence1," "))

def getSplit2(argSentence, argSplitList):
    word_li = []
    word = ""

    for char in argSentence:
        if  char not in argSplitList:
            word += char
        else:
            if word:
                word_li.append(word)
                word = ""
        # if char in argSplitList:
        #     if word:
        #         word_li.append(word)
        #         word = ""
        # else:
        #     word += char
    
    if word: 
        word_li.append(word)

    return word_li

sentence2 = '''hello he hehe    hellos  hellllo 
helowww hello hello hello
hello'''
split_li = ["\n", " ", "\t"]

print(getSplit2(sentence2, split_li))
