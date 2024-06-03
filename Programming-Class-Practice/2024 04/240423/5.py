# 아래 함수는 문자열을 입력 받아, 입력 받은 문자열의 길이를 반환하는 함수
foo = "hello"

def calculate_length(input_string):
    # 문자열의 길이를 구하는 함수를 직접 구현
    length = 0
    for _ in input_string:
        length += 1
    return length

foo = "hello"


# 함수를 사용하여 foo의 길이를 계산하고 출력
result = calculate_length(foo)



print("입력 받은 문자열의 길이:", result)

