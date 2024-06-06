while True:
    password_input = input("비밀번호를 입력하세요 : ")

    has_upper = False
    has_digit = False

    for char in password_input:
        if 'A' <= char <= 'Z':
            has_upper = True
        if '0' <= char <= '9':
            has_digit = True

    if len(password_input) < 8:
        print("비밀번호 길이 모자라요.")
    elif not has_upper:
        print("비밀번호 큰 일파벳 없습니다.")
    elif not has_digit:
        print("비밀번호 숫자 없습니다.")
    else:
        break

print("비밀본호가 안전합니다.")