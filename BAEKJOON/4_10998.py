result = 1

for number in range(1,3):
    number = int(input(f"{number}번째 의 값을 입력 해주세요\n"))
    result *= number

print(result)