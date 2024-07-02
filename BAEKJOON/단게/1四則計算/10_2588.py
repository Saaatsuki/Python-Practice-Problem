number1 = int(input("젓번째 3자리 정수를 입력해주세요 : "))
number2 = input("두번째 3자리 정수를 입력해주세요 : ")

a = int(number2[0])
b = int(number2[1])
c = int(number2[2])

answer1 = number1 * c
answer2 = number1 * b
answer3 = number1 * a

print(answer1,"\n"+str(answer2),"\n"+str(answer3))