# 사용자로부터 나이를 입력받습니다
age = int(input("나이를 입력하세요: "))

# 입력된 나이에 따라서 해당하는 그룹을 판별하고 출력합니다
if 13 <= age <= 19:
    print("You are in the 'Teenager' age group.")
elif 20 <= age <= 64:
    print("You are in the 'Adult' age group.")
elif age >= 65:
    print("You are in the 'Senior' age group.")
else:
    print("You are in the 'Unknown age group' age group.")


