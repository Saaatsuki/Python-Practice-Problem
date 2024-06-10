def sumNum(argFirst,argSecond):
    sum_num = argFirst + argSecond
    msg = "この値はマイナスです" if sum_num<0 else sum_num
    return msg
num1,num2 = map(int,input("2개 값을 입력해!! : ").split())
print(sumNum(num1,num2))

def sumNum(argFirst,argSecond):
    sum_num = argFirst + argSecond
    if sum_num<0 :
        print("この値はマイナスです") 
    else:
        return sum_num

num1,num2 = map(int,input("2개 값을 입력해!! : ").split())
print(sumNum(1,2))
print(sumNum(-1, -2))
print(sumNum(num1,num2))