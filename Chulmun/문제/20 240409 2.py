import random

def generate_password(length):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"

    all_characters = uppercase_letters + lowercase_letters + digits

    password = ""

    # 비밀번호 생성
    for _ in range(length):
        password += random.choice(all_characters)

    check1 = False  # 대문자 확인
    check2 = False  # 소문자 확인
    check3 = False  # 숫자 확인

    # 비밀번호 검증
    for char in uppercase_letters:
        if char in password:
            check1 = True
            break

    for char in lowercase_letters:
        if char in password:
            check2 = True
            break

    for char in digits:
        if char in password:
            check3 = True
            break

    # 검증을 통과하였으면 password를 반환 통과하지 못하였으면 함수를 재호출
    if check1 and check2 and check3:
        return password
    else:
        return generate_password(length)

# 입력
password_length = int(input("생성할 패스워드의 길이를 입력해주세요: "))

# 무한 반복을 막기 위하여 3자리 이상의 경우에만 동작
if password_length >= 3:
    generated_password =  generate_password(password_length)
    print(generated_password)
else:
    print("3자리 미만의 패스워드는 생성할 수 없습니다.")