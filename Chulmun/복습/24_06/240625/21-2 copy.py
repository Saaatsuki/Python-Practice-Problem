def getIndex_li_alp(sentence, word):
    index_li = []
    word_len = getLen(word) 
    sentence_len = getLen(sentence)  
    for i in range(sentence_len - word_len + 1):
            if sentence[i:i + word_len] == word:
                index_li.append(i)
    return index_li

def getIndex_li(argList, argVal):
    index_li = []
    for i in range(len(argList)):
        if argList[i] == argVal:
            index_li.append(i)  # append() メソッドを使用してインデックスをリストに追加
    return index_li  # ループが終わった後にリストを返す

def getSplit(argTxt, argSepList):
    word = ""
    word_li = []
    for char in argTxt:
        if not getIn(argSepList, char):
            word += char
        else:
            if word:
                word_li.append(word)
                word = ""
    if word:  # ループが終わった後に最後の単語を追加
        word_li.append(word)
    return word_li

def getLen(argList):
    length = 0
    for _ in argList:
        length += 1
    return length

def getCount(argList, argVal):
    count = 0
    for i in argList:
        if i == argVal:
            count += 1
    return count

def getIn(argList, argVal):
    for char in argList:
        if char == argVal:
            return True
    return False

sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

# 一文字毎のリスト
alp_li = [alp for alp in sentence]

# 単語毎のリスト
word_li = getSplit(sentence, [" ", "\n"])

alp = input("調べたい単語を入力してください：")
while not getIn(alp_li, alp):
    alp = input("入力された単語は存在しません。もう一度入力してください。\n調べたい単語を入力してください：")

# 入力された単語の個数
alp_count = getCount(word_li, alp)

# 全ての単語の個数
word_count = getLen(word_li)

# スペースの数
space_count = getCount(alp_li, " ")

# 行数
enter_count = getCount(alp_li, "\n")
line_count = enter_count + 1

# 全体の文字数
all_alp_count = getLen(alp_li) - (enter_count + space_count)

# 入力された単語の位置を取得(word_li)
index_place_IN_word_li = getIndex_li(word_li, alp)

# 入力された単語の位置を取得(alp_li)
index_place_IN_alp_li = getIndex_li_alp(sentence, alp)

print(f"入力された単語の個数：{alp_count}")
print(f"入力された単語の位置 (単語単位)：{index_place_IN_word_li}")
print(f"入力された単語の位置 (文字単位)：{index_place_IN_alp_li}")
print(f"全体の単語の個数：{word_count}")
print(f"全ての文字数：{all_alp_count}")
print(f"行数：{line_count}")