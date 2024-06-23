def getlen(arg):
    count = 0
    for _ in arg:
        count += 1
    return count

def getIn(argSmall, argBig):
    for i in argBig:
        if i == argSmall:
            return True
    return False
        
def getSum(argList):
    list_sum = 0
    for i in argList:
        list_sum += i
    return list_sum

sent = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

# 一文字毎のリストを作成
sent_alp_li = [alp for alp in sent]

# 単語毎のリストを作成
sent_word_li = []
word = ""
for alp in sent:
    if alp != " " and alp != "\t" and alp != "\n":
        word += alp
    else:
        if word:
            sent_word_li.append(word)
            word = ""
if word:
    sent_word_li.append(word)

user_word = input("単語を入力してください：")
while not getIn(user_word, sent_word_li):
    user_word = input("この単語は含まれていません。再度単語を入力してください：")

# 入力された単語の数
word_count = 0
for word in sent_word_li:
    if word == user_word:
        word_count += 1

# 入力された単語のIndexの値
word_index_li = []
for index, word in enumerate(sent_word_li):
    if word == user_word:
        ichi = getSum(getlen(word) + 1 for word in sent_word_li[:index])
        word_index_li.append(ichi)

# 単語自体の数
all_word_count = getlen(sent_word_li)

# 改行の数
enter_count = 0
for alp in sent_alp_li:
    if alp == "\n":
        enter_count += 1
enter_count_result = enter_count + 1

# スペースの数
space_count = 0
for alp in sent_alp_li:
    if alp == " ":
        space_count += 1

# 全体の文字数
alp_count_all = getlen(sent_alp_li)
alp_count = alp_count_all - (enter_count + space_count)

print(f"入力された単語の数：{word_count}")
print(f"入力された単語の位置：{word_index_li}")
print(f"全体の単語の数：{all_word_count}")
print(f"全体の文字の数：{alp_count}")
print(f"改行の数：{enter_count_result}")