def getSplit(argSentence, argSplit):
    word_li = []
    word = ""

    for char in argSentence:
        if char != argSplit:
            word += char
        else:
            if word:
                word_li.append(word)
                word = ""
    
    if word: 
        word_li.append(word)
    
    return word_li
