number1 = int(input("첫 번째 값을 입력 하세요 : "))
number2 = int(input("두 번째 값을 입력 하세요 : "))

calculation = input("연산자를 입력 하세요 (+,-,*,/, 증 하나 입력) : ")


if (calculation == "+"):
    add = number1 + number2
elif (calculation == "-"):
    sub = number1 - number2
elif (calculation == "*"):
    mul = number1 * number2
elif (calculation == "/"):
    div = number1 / number2
    

res = input("결과 값 자료형 (integer,float,string 증 하나 입력 : ")

if (res == "integer"):
    if (calculation == "+"):
        result = int(add)
    elif (calculation == "-"):
        result = int(sub)
    elif (calculation == "*"):
        result = int(mul)
    elif (calculation == "/"):
        result = int(div)
elif (res == "float"):
    if (calculation == "+"):
        result = float(add)
    elif (calculation == "-"):
        result = float(sub)
    elif (calculation == "*"):
        result = float(mul)
    elif (calculation == "/"):
        result = float(div)    
elif (res == "string"):
    if (calculation == "+"):
        result = str(add)
    elif (calculation == "-"):
        result = str(sub)
    elif (calculation == "*"):
        result = str(mul)
    elif (calculation == "/"):
        result = str(div)       
        

print("결과 값은 아래 같습니다.")
print(number1 ,calculation,number2,"=",result)