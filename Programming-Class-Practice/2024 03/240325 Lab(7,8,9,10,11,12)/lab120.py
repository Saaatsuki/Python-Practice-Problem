# 소득세를 계산하는 함수를 정의합니다.
def calculate_income_tax(income):
    # 소득이 1만 달러 이하인 경우
    if (income <= 10000):
        return income * 0.1
    # 소득이 1만 달러 초과 2만 달러 이하인 경우
    elif (10000 < income <= 20000):
        return (income - 10000) * 0.15 + 1000
    # 소득이 2만 달러를 초과하는 경우
    else:
        return (income - 20000) * 0.20 + 2500


# 사용자로부터 소득을 입력받습니다.
income = float(input("소득 금액을 입력해주세요: "))

# 소득세를 계산합니다.
income_tax = calculate_income_tax(income)

# 소득세를 출력하기 위한 형식 지정 문자열입니다.
msg = "소득세는 {}달러 입니다."

# 계산된 소득세를 출력합니다.
print(msg.format(income_tax))
