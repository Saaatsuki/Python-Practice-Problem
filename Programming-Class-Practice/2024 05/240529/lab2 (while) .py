# 변주 "number"를 설정
number = 1
# 변주 "sum3"를 설정
sum3 = 0

# 0~1000 정수를 "number"로 성절한다 
while (0 < number <1000):
    # 만아게 number가 3의 배수이라면 구한다
    if (number%3==0):
        sum3 += number
    number += 1

print(f"1~1000 사이 정수 중 3의 배수의 총 합은 : {sum3}")
