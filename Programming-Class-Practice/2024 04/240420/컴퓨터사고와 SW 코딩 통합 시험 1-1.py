numbers = []

for i in range(1,6):
    number = int(input(f"{i}번째 값 입력"))
    numbers.append(number)

add = sum(numbers)
avarage = add / 5
print("합계 : ",add)
print("평균 : ",avarage)
