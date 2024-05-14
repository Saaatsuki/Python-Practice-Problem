numbers = []

for number in range(1,3):
    number = int(input(f"{number}번째의 정수 를 인력 해주세요\n"))
    numbers.append(number)
    
print(sum(numbers))