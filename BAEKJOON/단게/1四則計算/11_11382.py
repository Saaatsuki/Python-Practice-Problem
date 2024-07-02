numbers = []

for i in range(1,4):
    number = int(input(f"{i}번째 정수를 입력 해주세요 : "))
    numbers.append(number)
    
answer = sum(numbers)


result = 0
for n in numbers:
    result += n
    
print(result)