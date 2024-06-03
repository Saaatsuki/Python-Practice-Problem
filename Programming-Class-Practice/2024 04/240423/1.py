# 정수 3개를 입력 받아서 제일 큰 값을 출력하시요?

# 3つの整数を受け取る
number1 = int(input("1番目の整数を入力してください："))
number2 = int(input("2番目の整数を入力してください："))
number3 = int(input("3番目の整数を入力してください："))

#　max関数を使ったやり方①
print(max(number1,number2,number3))

#　ifを使ったやり方②

if (number1 >= number2 and number1 >= number3):
    print(number1)
elif (number2 >= number1 and number2 >= number3):
    print(number2)
elif (number3 >= number1 and number3 >= number2):
    print(number3)
    
#　やり方③
max = number1

if max < number2:
    max = number2

if max < number3:
    max = number3
    
print(max)

# やり方④
max = -1

for trial_count in range(1, 4):
    msg = str(trial_count) + "번"
    input_value = int(input(msg))
    
    if max < input_value:
        max = input_value
    
print(max)

