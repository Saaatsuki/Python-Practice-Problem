while True:
    input_password = input("비밀본호 입력하세요 : ")

    alp_tf = False
    num_tf = False

    for i in input_password:
        if 'A' <= i <= 'Z':
            alp_tf = True
        if '0' <= i <= '9':
            num_tf = True

    if alp_tf and num_tf and len(input_password)>=8:
        print("비밀번호가 안전합니다.")
        break
    elif alp_tf == False and num_tf == False:
        print("숫자과 큰 알파벳이 없습니다.")
    elif not alp_tf:
        print("큰 알파벳이 없습니다.")
    elif not num_tf:
        print("숫자가 없습니다.")
    elif not len(input_password)>=8:
        print("길이가 모자라합니다")