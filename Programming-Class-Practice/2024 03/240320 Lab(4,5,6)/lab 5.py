# 사용자로부터 성별을 한글로 입력받습니다
gender_korean = input("성별을 한글로 입력하세요 (남자/여자): ")

# 입력된 성별에 따라 영어로 변환하여 출력합니다
if gender_korean == "남자":
    print("MAN")

elif gender_korean == "여자":
    print("WOMAN")

else:
    print("잘못된 입력입니다.")