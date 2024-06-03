number1 = int(input("첫 번째 값을 입력 하세요 : "))
number2 = int(input("두 번째 값을 입력 하세요 : "))

calculation = input("연산자를 입력 하세요 (+,-,*,/, 증 하나 입력) : ")

if (calculation == "+"):
    cal_result = number1 + number2
elif (calculation == "-"):
    cal_result = number1 - number2
elif (calculation == "*"):
    cal_result = number1 * number2
elif (calculation == "/"):
    cal_result = number1 / number2
    

res = input("결과 값 자료형 (integer,float,string 증 하나 입력 : ")

if (res == "integer"):
    result = int(cal_result)
elif (res == "float"):
    result = float(cal_result)
elif (res == "string"):
    result = str(cal_result)
        

print("결과 값은 아래 같습니다.")
print(number1 ,calculation,number2,"=",result)