numbers = []

for i in range(1,4):
    number = int(input(f"{i}番目のサイコロの目を入力してください："))
    numbers.append(number)
    
num1 = numbers[0]
num2 = numbers[1]
num3 = numbers[2]

if (num1 == num2 == num3):
    money = num1 * 1000 + 10000
elif((num1 == num2)or(num1 == num3)):
    money = num1 * 100 + 1000
elif(num2 == num3):
    money = num2 * 100 + 1000
else:
    money = max(numbers) * 100

print(money,"₩")