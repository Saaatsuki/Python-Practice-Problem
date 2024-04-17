# 섭씨를 화씨로 변환하는 함수를 정의합니다.
def celsius_to_fahrenheit(celsius):
    # 화씨 온도 = (섭씨 온도 × 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# 사용자로부터 섭씨 온도를 입력받습니다.
celsius_input = int(input("섭씨 온도를 입력해주세요: "))

# 입력된 섭씨 온도를 화씨로 변환합니다.
fahrenheit_output = celsius_to_fahrenheit(celsius_input)

# 변환된 화씨 온도를 출력합니다.
print("화씨 온도는", fahrenheit_output, "도입니다.")