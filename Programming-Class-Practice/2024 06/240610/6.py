def sumAvg(arg1,arg2,arg3,arg4):
    li = [arg1,arg2,arg3,arg4]
    sum_arg = 0
    [sum_arg:=sum_arg + i for i in li]
    avg_arg = sum_arg / len(li)
    return sum_arg,avg_arg

num1,num2,num3,num4 = map(int,input("4개 정수를 입력하세요 : ").split())
print(sumAvg(num1,num2,num3,num4))

sum,avg = sumAvg(1,2,3,4)
print(sum,avg)
value = sumAvg(1,2,3,4)
print(value[0],value[1])