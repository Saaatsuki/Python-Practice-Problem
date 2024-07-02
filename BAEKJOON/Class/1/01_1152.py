def getSplit(argTxt,argSep):
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
    return word_li

txt = input()
print(len(getSplit(txt," ")))