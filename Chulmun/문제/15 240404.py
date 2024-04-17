baseValue = float(input("Please enter base price : "))

# 演算を選択する関数
def selectOperation():
    
    # グローバル変数 baseValue を関数内で使用
    global baseValue
   
    # 演算の種類
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")
    select = int(input("Please enter your select number : "))
    number = float(input("Please enter your favorite number : "))
    msg = "arithmetic result : {}"
    if (select == 1):
        print (msg.format(baseValue + number))
    elif (select == 2):
        print (msg.format(baseValue - number))
    elif (select == 3):
        print (msg.format(baseValue * number))
    elif (select == 4):
        if (number != 0):
            print(msg.format(baseValue / number))
        else:
            print("Error : You can't divide it by 0")
                

selectOperation()