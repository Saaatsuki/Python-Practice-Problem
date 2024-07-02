num1 , num2 = input().split()

number1 = int(num1[2]+num1[1]+num1[0])
number2 = int(num2[2]+num2[1]+num2[0])
# number1 = int(num1[::-1])  # num1を逆順にして整数に変換
# number2 = int(num2[::-1])  # num2を逆順にして整数に変換

if number1>number2:
    print(number1)
else:
    print(number2)