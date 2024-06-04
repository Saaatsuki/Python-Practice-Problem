import random

user_input_list = []

# ユーザーから3つの単語を収集し、長さの制約をチェックします。
for i in ["첫", "두", "세"]:
    user_input = input(f"{i} 번째 단어를 입력하세요: ")  # {i} 番目の単語を入力してください
    user_input_len = len(user_input)
    
    # 単語の長さが5文字以上20文字以下であることを確認します。
    while not (5 <= user_input_len <= 20):
        user_input = input("단어는 5자 이상 20자 이하이어야 합니다. 다시 입력해주세요: ")  # 単語は5文字以上20文字以下である必要があります。再入力してください。
        user_input_len = len(user_input)
    
    user_input_list.append(user_input)

# ユーザーの単語からランダムに1つを選択します。
pc_random_word = random.choice(user_input_list)
print(f"단어 선택 완료. 게임을 시작합니다. 선택된 단어: {pc_random_word}")  # 単語の選択が完了しました。ゲームを開始します。選ばれた単語: {pc_random_word}

# 選ばれた単語を文字のリストに変換します。
pc_random_word_list = list(pc_random_word)
pc_random_word_len = len(pc_random_word)
blind_number = (pc_random_word_len + 1) // 2  # ブラインドする文字の数を計算します。

# ブラインドするインデックスをランダムに選びます。
blind_indices = random.sample(range(pc_random_word_len), blind_number)
blinded_word_list = pc_random_word_list[:]

# 選ばれたインデックスの文字をブラインドします。
for index in blind_indices:
    blinded_word_list[index] = '_'

print("블라인드된 단어:", ''.join(blinded_word_list))  # ブラインドされた単語を表示します。

attempts = 0

# ユーザーの入力とブラインド解除
while '_' in blinded_word_list:
    guess = input("알파벳을 한 글자 입력하세요: ")  # アルファベットを1文字入力してください
    
    if len(guess) != 1 or not guess.isalpha():
        print("한 글자의 알파벳을 입력하세요.")  # 1文字のアルファベットを入力してください。
        continue

    attempts += 1
    if guess in pc_random_word:
        for index in blind_indices:
            if pc_random_word_list[index] == guess:
                blinded_word_list[index] = guess
                blind_indices.remove(index)  # 正解したら、ブラインドリストから削除
        print("현재 단어: " + ''.join(blinded_word_list))  # 現在の単語を表示します。
    else:
        print("없음")  # なし
        
print(f"축하합니다! 단어를 맞췄습니다: {pc_random_word}")  # おめでとうございます！単語を当てました。
print(f"시도 횟수: {attempts}")  # 試行回数を表示します。
