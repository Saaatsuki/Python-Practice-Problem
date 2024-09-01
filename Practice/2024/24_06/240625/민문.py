def getSum(argList):
    sum = 0
    for i in argList:
        sum += i
    return sum

def getSplit(argTxt,argSep):
    word = ""
    word_li = []
    for char in argTxt:
        if char != argSep:
            word += char
        else:
            if word:
                word_li.append(word)
                word = ""
    if word:
        word_li.append(word)
    return word_li

def Fevonach(argLen):
    fevo_li = [1,1]
    for index in range(2,argLen):
        num = fevo_li[index-2] + fevo_li[index-1]
        index += 1
        fevo_li.append(num)
    return fevo_li

def getJoin(argList,argSep):
    join = ""
    index = 0
    while index<len(argList):
        join += str(argList[index])
        index += 1
        if index<len(argList):
            join += argSep
    return join
    
while True:
    menu = int(input("\nメニュー:\n\
1. 四則演算計算機\n\
2. リストの合計計算\n\
3. フィボナッチ数列の出力\n\
4. 終了\n\
希望する機能を選んでください: "))
    
    if menu == 1:
        num1 = int(input("最初の数字を入力してください : "))
        num2 = int(input("2番目の数字を入力してください :"))
        cal = input("演算子を入力してください (+, -, *, /) : ")
        while not cal in ["+","-", "*", "/"]:
            cal = input("必ず演算子を入力してください (+, -, *, /) : ")
        while num2 == 0 and cal == "/":
            num2 = int(input("0以外の2番目の数字を入力してください :"))
        
        if cal == "+":
            res = f"{num1} + {num2} = {(num1 + num2)}"
        elif cal == "-":
            res = f"{num1} - {num2} = {(num1 - num2)}"
        elif cal == "*":
            res =f"{num1} X {num2} = {(num1 * num2)}"
        else :
            res =f"{num1} ÷ {num2} = {(num1 / num2)}"
        print(res)

    elif menu == 2:
        num_txt = input("整数リストを入力してください（カンマで区切り、例: 1,2,3,4）: ")
        num_li = getSplit(num_txt,",")
        num_int_li = [int(num) for num in num_li]

        num_sum = getSum(num_int_li)
        print(f"リストの合計：{num_sum}")

    elif menu == 3:
        lengh = int(input("フィボナッチ数列の長さを入力してください："))
        print(f"フィボナッチ数列 : {getJoin(Fevonach(lengh),',')}")

    elif menu == 4:
        print("プログラムを終了します。")
        break

    else:
        print("1~4からメニューを選択してください。")