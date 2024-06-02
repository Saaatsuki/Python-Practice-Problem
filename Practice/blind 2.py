import random

user_input_list = []

# ユーザーから3つの単語を収集し、長さの制約をチェックします。
for i in ["첫", "두", "세"]:
    user_input = input(f"{i} 번째 단어를 입력하세요\n")  # {i} 番目の単語を入力してください
    user_input_len = len(user_input)
    
    # 単語の長さが3文字以上20文字以下であることを確認します。
    while not (3 <= user_input_len <= 20):
        user_input = input("3이상 20이하 글자로 구성된 단어를 입력 하세요\n")  # 3以上20以下の文字で構成された単語を入力してください
        user_input_len = len(user_input)
    
    user_input_list.append(user_input)

# ユーザーの単語からランダムに1つを選択します。
pc_random_word = random.choice(user_input_list)
print(f"단어 선택 완료 게임 시작합니다. 선택된 단어 : {pc_random_word}")  # 単語の選択が完了しました。ゲームを開始します。選ばれた単語: {pc_random_word}

# 選ばれた単語を文字のリストに変換します。
pc_random_word_list = list(pc_random_word)
pc_random_word_len = len(pc_random_word)
blind_number = int(pc_random_word_len * 0.5 + 0.5)  # ブラインドする文字の数を計算します。

blind_list = []
# 選ばれた単語からランダムに文字をブラインドします。
for _ in range(blind_number):
    index = random.randint(0, len(pc_random_word_list) - 1)  # randintの範囲を修正
    blind_list.append(pc_random_word_list[index])
    del pc_random_word_list[index]
print(blind_list)  # ブラインドされた文字を表示します。

for i in blind_list:
    pc_random_word_list[i]="_"