# 사용자에게 현재 연도를 입력하도록 요청합니다.
current_year = int(input("현재 연도를 입력하십시오:"))

# 사용자에게 태어난 연도를 입력합니다.
birth_year = int(input("태어난 연도를 입력하세요:"))

# 나이를 계산합니다.
age = current_year - birth_year

# 나이를 출력합니다.
print("나이는" , age , "세입니다.")