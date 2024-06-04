import random

# 英単語を保管するリストを作成する
alphabets = []
input_msg = "{}番目の英単語を入力してください : "

# 3つの英単語を受け取る
for i in ["一", "二", "三"]:
    alp = input(input_msg.format(i))
    while not 3 <= len(alp) <= 20:
        alp = input("3以上20以下の文字数の英単語を入力してください\n")
        
    alphabets.append(alp)

    
# 3つの英単語のうち、パソコンがランダムでひとつの英単語を選択する
select_word = random.choice(alphabets)
print("単語選択完了ゲームを始めます。選択した単語：", select_word)

# 選択した単語の文字の50％を"_"に変更する
select_word_length = len(select_word)
underbar = int(select_word_length * 0.5 + 0.5)
indices = set()

while len(indices) < underbar:
    index = random.randint(0, select_word_length - 1)
    indices.add(index)

# リストに変換して文字を置き換える
select_word_list = list(select_word)

for i in indices:
    select_word_list[i] = "_"

# Listの文字列を結合し、出力する
behind_word = "".join(select_word_list)
print("変更後の単語：", behind_word)

game_number = 0
while "_" in behind_word:
    
    game_number += 1
    in_word = input(f"{game_number}回目の試み：下の単語を構成しているアルファベットをひとつ入力してください\n{behind_word}\n")

    count = 0
    if in_word in select_word:
        # 正しいアルファベットが入力された場合、そのアルファベットをすべて表示する
        for i in range(select_word_length):
            if select_word[i] == in_word:
                select_word_list[i] = in_word
                count += 1
                print(f"入力したアルファベットの内含まれている単語：{count}文字")
        behind_word = "".join(select_word_list)

    else:
        print("残念：入力したアルファベットはこの単語に含まれません")
        continue
print(f"Clear!!!選択された単語{select_word},試行回数：{game_number}")        