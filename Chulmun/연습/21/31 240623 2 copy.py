def getlen(arg):
    return len(arg)

def getIn(argSmall , argBig):
    indices = []
    for idx, word in enumerate(argBig):
        if word == argSmall:
            indices.append(idx)
    return indices

sent = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

# 文章を一文字ずつリストに分割する
sent_alp_li = [char for char in sent]

# 文章を単語のリストに分割する
sent_word_li = sent.split()

# ユーザーからの入力
user_word = input("単語を入力してください: ")
while user_word not in sent_word_li:
    user_word = input("その単語は見つかりませんでした。もう一度単語を入力してください: ")

# 単語の出現回数と位置を数える
word_count = sent_word_li.count(user_word)
word_index_li = getIn(user_word, sent_word_li)

# 単語の位置を文字のリストのインデックス位置に変換する
word_index_li_alp = []
for index in word_index_li:
    # 単語の位置を計算する
    position = sum(len(word) + 1 for word in sent_word_li[:index])
    word_index_li_alp.append(position)

# 全体の単語数を数える
all_word_count = len(sent_word_li)

# 改行の数を数える
enter_count_result = sent.count('\n') + 1

# スペースと改行を除いた文字数を数える
alp_count = sum(1 for char in sent if char not in ' \n')

# 結果を出力する
print(f"単語 '{user_word}' の出現回数: {word_count}")
print(f"単語 '{user_word}' の位置（文字のリストのインデックス位置）: {word_index_li_alp}")
print(f"全体の単語数: {all_word_count}")
print(f"全体の文字数: {alp_count}")
print(f"改行の数: {enter_count_result}")
