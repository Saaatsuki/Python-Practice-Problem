import random

input_list3 = []
    
for i in ["첫", "두", "세"]:
    input_word = input(f"{i} 번째 단어를 입력해주세요\n")
    input_word_len = len(input_word)
    
    while not (3 <= input_word_len <= 20):
        input_word = input("3이상 20이하 글자로 구성된 단어를 입력 하세요\n")
        input_word_len = len(input_word)
        
    input_list3.append(input_word)
    
pc_random_word = random.choice(input_list3)
print(f"단어 선택 완료 게임을 시작합니다. 선택된 단어: {pc_random_word}")

pc_random_word_len = len(pc_random_word)
blind_count = int(pc_random_word_len * 0.5 + 0.5)
pc_random_word_list = list(pc_random_word)
print(f"선택된 단어 리스트: {pc_random_word_list}")

blind_choice = random.sample(range(pc_random_word_len), blind_count)
print(f"블라인드 처리할 인덱스: {blind_choice}")


pc_random_word_list_blind = pc_random_word_list.copy()
for i in blind_choice:
    pc_random_word_list_blind[i] = "_"
print(f"블라인드 처리된 단어 리스트: {pc_random_word_list_blind}")

pc_random_word_blind_join = " ".join(pc_random_word_list_blind)
print(f"블라인드 처리된 단어: {pc_random_word_blind_join}")

game_count = 0
while "_" in pc_random_word_list_blind:
    game_count += 1
    user_word = input(f"{game_count}번째 시도, 아래 단어를 구성하는 알파벳 한개 입력하세요\n{pc_random_word_blind_join}\n")
    user_word_count = 0
    for index, char in enumerate(pc_random_word_list):
        if user_word == char:
            pc_random_word_list_blind[index] = user_word
            user_word_count += 1
    
    if user_word_count > 0:
        print(f"입력한 알파벳 단어 내 포함: {user_word_count}글자")
    else:
        print("단어 내 포함되지 않은 알파벳 입니다")
    
    pc_random_word_blind_join = " ".join(pc_random_word_list_blind)
    print(f"현재 상태: {pc_random_word_blind_join}")
            
print(f"Clear!!! 선택된 단어: {''.join(pc_random_word_list)} , 총 시도 횟수: {game_count}")
