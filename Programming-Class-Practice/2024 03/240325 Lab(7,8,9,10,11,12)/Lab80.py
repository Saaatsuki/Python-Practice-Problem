# 사용자로부터 하나의 영문자를 입력받습니다.
alphabet = input("한 영문자를 해주세요 : ")

# 모음에 대한 메시지を事前に 구성합니다.
msg = alphabet,"는 모음입니다."


# 입력된 알파벳이 모음인지 확인합니다.
if (alphabet == "a"):
    print(msg)
elif (alphabet == "e"):
    print(msg)
elif (alphabet == "i"):
    print(msg)
elif (alphabet == "o"):
    print(msg)
elif (alphabet == "u"):
    print(msg) 
else:
    print(alphabet,"는 모음이 마닙니다.")