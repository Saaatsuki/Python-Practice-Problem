# 사용자로부터 소득 금액을 입력받습니다.
income = float(input("소득 금액을 입력해주세요: "))

# 소득세를 출력하기 위한 형식 지정 문자열입니다.
msg = "소득세는 {}달러 입니다."

# 소득에 따라 적절한 소득세를 계산하고 출력합니다.

if (income <= 10000):
    print(msg.format(income*0.1))
elif(10000 < income <= 20000):
    print(msg.format((income-10000)*0.15+1000))
elif(20000 < income):
    print(msg.format((income-20000)*0.20+2500))