num1 = int(input("첫 번째 숫자(정수)를 입력하세요 : "))
num2 = float(input("첫 번째 숫자(정수)를 입력하세요 : "))
msg = "이하" if num1+num2<100 else "초과"
print(f"합이 100 {msg}합니다 : {num1+num2:.1f}")