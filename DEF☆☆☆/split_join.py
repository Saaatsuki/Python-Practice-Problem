def getSplit(argSentence, argSplit):
    word_li = []  # 分割された単語を格納するリスト
    word = ""     # 単語の文字列を累積する変数

    for char in argSentence:
        if char != argSplit:
            word += char  # 文字が区切り文字でない場合、単語に文字を追加
        else:
            if word:
                word_li.append(word)  # 単語があればリストに追加し、単語変数をリセット
                word = ""  # 単語変数を空にする
    
    if word:
        word_li.append(word)  # 最後の単語をリストに追加する
    
    return word_li  # 分割された単語のリストを返す

# 使用例:
sent = input("文章を入力してください：")
result = getSplit(sent, ",")
print(result)

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




# join() → def getJoin()
def getJoin(argList, separator):
    result = ""
    index = 0
    while index < len(argList):
        result += argList[index]
        index += 1
        if index < len(argList):
            result += separator
    return result

# ユーザーによって入力された文字列リストを取得
txt_list = input("文字列リストをスペースで区切って入力してください: ").split()

# 自作のjoin関数を使用してリストの文字列を連結
joined_string = getJoin(txt_list, " ")

# 結果を出力
print("連結された文字列:", joined_string)