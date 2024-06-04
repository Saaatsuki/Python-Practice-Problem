import random

def get_valid_word(prompt):
    while True:
        word = input(prompt)
        if 5 <= len(word) <= 20:
            return word
        print("単語は5文字以上20文字以下である必要があります。再入力してください。")

def blind_word(word):
    word_list = list(word)
    word_length = len(word)
    blind_count = (word_length + 1) // 2  # 切り上げ
    blind_indices = random.sample(range(word_length), blind_count)
    
    for index in blind_indices:
        word_list[index] = '_'
        
    return ''.join(word_list), set(blind_indices)

def main():
    words = []
    for i in range(1, 4):
        words.append(get_valid_word(f"{i} 番目の単語を入力してください: "))
    
    chosen_word = random.choice(words)
    print(f"選ばれた単語: {chosen_word}")

    blinded_word, blind_indices = blind_word(chosen_word)
    print(f"ブラインドされた単語: {blinded_word}")

    attempts = 0
    guessed_word = list(blinded_word)

    while '_' in guessed_word:
        guess = input("アルファベットを1文字入力してください: ")
        
        if len(guess) != 1 or not guess.isalpha():
            print("1文字のアルファベットを入力してください。")
            continue

        attempts += 1
        if guess in chosen_word:
            for index in blind_indices:
                if chosen_word[index] == guess:
                    guessed_word[index] = guess
                    blind_indices.remove(index)  # 正解したら、ブラインドリストから削除
            print("現在の単語: " + ''.join(guessed_word))
        else:
            print("なし")
        
    print(f"おめでとうございます！単語を当てました: {chosen_word}")
    print(f"試行回数: {attempts}")

if __name__ == "__main__":
    main()
