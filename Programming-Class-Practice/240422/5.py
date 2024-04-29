number1 = float(input("一番目の値を入力してください\n"))
number2 = float(input("二番目の値を入力してください\n"))

cal = input("演算方法を選んでください（+-*/）\n")

met = input("結果の値の種類をえらんでください（integer,float,string）\n")

if (cal == "+"):
    res = number1 + number2
elif (cal == "-"):
    res = number1 - number2
elif (cal == "*"):
    res = number1 * number2
elif (cal == "/"):
    if (number2 == 0):
        exit()
    res = number1 * number2

if (met == "integer"):
    print(number1,cal,number2,"=",int(res))
elif (met == "float"):
    print(number1,cal,number2,"=",float(res))    
elif (met == "string"):
    print(number1,cal,number2,"=",str(res))

        