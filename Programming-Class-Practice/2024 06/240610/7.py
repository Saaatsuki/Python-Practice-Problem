numbers = {}
for i in range(4):
    num = int(input(f"{i+1}번째의 정수를 입력하세요 : "))
    numbers[f"{i+1}"]=num
print(numbers)