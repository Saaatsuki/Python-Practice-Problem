# 요구사항
# 1. 미리 입력된 문장에서 검색 문자열을 입력받고,
# 2. 입력된 문자열이 있을 경우 검색 결과를 출력한 후 프로그램을 종료
# 3. 만약 검색된 결과가 없을 경우 검색 문자를 재입력 받는다

# 문자열 검색을 위한 사전 입력 문장
sentence = """          pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

# 개행 문자가 포함된 여러 줄 문자열 출력
# print(sentence)

# """ """ 구문은 여러 줄 문자열(Multiline string)을 정의하는데 사용된다
# 이를 활용하여 개행 문자가 포함된 여러 줄 문자열을 효율적으로 작성할 수 있다

word = "" # 단어
sentence_list = [] # sentence를 list 화 시키기
line = 1 # 줄 수
index = 0
index_list = [0] # 단어가 들어가 있는 전체 index 리스트
# 전체 문자 수를 위한 변수 설정
all_word = 0 # 총 문자수
spacebar = 0 # 띄어쓰기
gaehangword = 0 # 개행 문자


for i in sentence:
    
    # 빈칸을 만났을경우 + word에 단어가 있을경우
    if i == " "  and word != "":
        sentence_list.append(word)
        word = ""
        index += 1
        index_list.append(index)
        spacebar += 1
    
    # 빈칸을 만났을경우 + word에 단어가 없을경우 (스페이스바 2번 이상)
    elif i == " " and word == "":
        index += 1
        spacebar += 1

    # 열이 끝났을때
    elif i =="\n":
        # word에 단어를 추가
        if word:
            sentence_list.append(word)
            word = ""
            index_list.append(index+1)
        line += 1 # 열이 끝났을때 줄 수를 1추가
        index += 5
        gaehangword += 1
    
    # 단어일 경우
    else:
        word += i # word에 해당 단어를 추가
        index += 1
    
    all_word += 1 # 총 문자수 += 1

# 반복문이 끝나고 마지막 단어 추가
if word:
    sentence_list.append(word)
    index_list.append(index)

# 전체 문자 수 계산
really_all_word = all_word - spacebar - gaehangword

# 문자열 검색
while True:
    user_input = input("검색할 문자열을 입력하세요: ")
    
    # 문자열이 sentence_list에 없을 경우
    if user_input not in sentence_list:
        print("해당 문자열이 없습니다. 다시 입력해주세요.")
        continue
    
    count_word = 0 # 검색된 문자열의 갯수
    index = 0 # 해당 단어가 있는 index 번호
    index_list1 =[] # 해당 단어가 있는 index 번호 추가
    
    for i in sentence_list:
        # 검색한 문자열이 맞는 경우
        if i == user_input:
            count_word += 1 # 검색된 문자 + 1
            index_list1.append(index_list[index])

        # 아닌경우는 그냥 index만 + 1
        index += 1
            
    
    print(f"검색된 문자열의 개수: {count_word}")
    print(f"검색된 문자열의 위치: {index_list1}")
    print(f"단어의 개수: {index}")
    print(f"전체 문자 수: {really_all_word}")
    print(f"줄 수: {line}")
    break
