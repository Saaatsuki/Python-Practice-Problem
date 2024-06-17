def calculate_avarage(*argList):

    sum = 0
    for value in argList:
        sum += value
    return sum / len(argList)

    # argList_sum = 0
    # [argList_sum:=argList_sum+i for i in argList] 
    # return f"{(argList_sum / len(argList)):.1f}"
print(calculate_avarage(1,2,3,4,5))
print(calculate_avarage(6,7,8))
print(calculate_avarage(10,20))