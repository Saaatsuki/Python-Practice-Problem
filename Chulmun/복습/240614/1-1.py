age = int(input("사용자의 나이를 입력해주세요 : "))
msg = "어린이" if age<=12 else "청소년" if 13<=age<=18 else "성인" 
print(f"{msg} 이용권을 사용할 수 있습니다 . ")