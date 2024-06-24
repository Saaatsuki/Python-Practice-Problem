user_age = int(input("사용자의 나이를 입력하세요 : "))
msg = "어린이" if user_age<=12 else "정소년" if 13<=user_age<=18 else "성인"
print(f"{msg} 이용권을 사용할 수 있습니다.")
