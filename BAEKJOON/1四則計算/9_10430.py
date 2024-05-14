numbers = []
for i in range (1,4):
    number = int(input(f"{i}번째의 값을 입력 해주세요 : "))
    numbers.append(number)

a = numbers[0]
b = numbers[1]
c = numbers[2]

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)