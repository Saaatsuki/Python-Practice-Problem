numbers = []
for number in range (1,3):
    number = int(input(f"{number}번째의 정수를 입력 해주세요:"))
    numbers.append(number)
    
print(sum(numbers))
