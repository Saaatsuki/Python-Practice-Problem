numbers = []

for i in range(1,3):
    number = int(input(f"{i}번째 정수를 입력해주세요 : "))
    numbers.append(number)

a = numbers[0]
b = numbers[1]

if (a < b):
    print("<")
elif(a > b):
    print(">")
else:
    print("==")