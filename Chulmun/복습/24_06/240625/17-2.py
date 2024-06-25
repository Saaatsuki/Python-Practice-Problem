import random
import math

def input_words():
    words = []
    while len(words) < 3:
        word = input(f"영어 단어 {len(words) + 1} 입력 (5~20자 이내): ")
        if len(word) < 5 or len(word) > 20:
            print("단어의 길이가 유효 범위를 벗어났습니다. 다시 입력하세요.")
        else:
            words.append(word)
    return words

def select_word(words):
    return random.choice(words)

def calculate_blind_length(word):
    word_length = len(word)
    blind_length = math.ceil(word_length / 2)
    return blind_length

def apply_blind(word, blind_length):
    word_list = list(word)
    blind_indices = random.sample(range(len(word)), blind_length)
    for idx in blind_indices:
        word_list[idx] = '_'
    return ''.join(word_list)

def check_letter(word, letter, revealed_word):
    if letter in word:
        indices = [i for i, char in enumerate(word) if char == letter]
        for idx in indices:
            revealed_word[idx] = word[idx]
        return True
    else:
        return False

def main():
    print("단어 맞추기 게임을 시작합니다.\n")
    words = input_words()
    selected_word = select_word(words)
    print(f"\n선택된 단어: {selected_word}\n")
    
    blind_length = calculate_blind_length(selected_word)
    blind_word = apply_blind(selected_word, blind_length)
    print(f"Blind 처리된 단어: {blind_word}\n")
    
    revealed_word = ['_' if char == '_' else None for char in blind_word]
    attempt_count = 0
    
    while '_' in revealed_word:
        attempt_count += 1
        guess_letter = input("알파벳 한 글자를 입력하세요: ").lower()
        
        if len(guess_letter) != 1 or not guess_letter.isalpha():
            print("올바른 알파벳 한 글자를 입력하세요.")
            continue
        
        if check_letter(selected_word, guess_letter, revealed_word):
            print("알파벳을 맞췄습니다!\n")
        else:
            print("해당 알파벳은 단어 안에 없습니다.\n")
        
        current_word = ''.join([char if char is not None else '_' for char in revealed_word])
        print(f"현재 단어 상태: {current_word}\n")
    
    print(f"축하합니다! 단어를 맞추셨습니다. 시도 횟수: {attempt_count}")

if __name__ == "__main__":
    main()
