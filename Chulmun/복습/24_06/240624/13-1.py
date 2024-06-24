def getSplit(argSentence,argSplit):
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

def getIn(argSequence,argCheck):
    for val in argSequence:
        if val == argCheck:
            return True
    return False

def getCount(argSequence,argCheck):
    count = 0
    for val in argSequence:
        if val == argCheck:
            count += 1
    return count


while True:
    txt = input("文章を入力するちゃむ💛：")
    txt_li = getSplit(txt," ")
    while True:
        word = input("確認したい単語を入力するちゃむ💛：")
        if not getIn(txt_li,word):
            print("この単語は含まれてないちゃむよ")
        else:
            print(f"{word}の出力頻度：{getCount(txt_li,word)}")
            break