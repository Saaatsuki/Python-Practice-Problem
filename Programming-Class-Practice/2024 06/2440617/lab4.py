def max_of_three(argNum1,argNum2,argNum3):

    if argNum1 >= argNum2 and argNum1 >= argNum3:
        return argNum1
    elif argNum2 >= argNum1 and argNum2 >= argNum3:
        return argNum2
    else:
        return argNum3
    
    # max_num = argNum1
    # for i in [argNum1,argNum2,argNum3]:
    #     if max_num<i:
    #         max_num=i
    # return max_num
print(max_of_three(10,20,15))
