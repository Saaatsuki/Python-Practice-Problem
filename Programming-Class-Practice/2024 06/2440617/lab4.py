def max_of_three(argNum1,argNum2,argNum3):
    max_num = argNum1
    for i in [argNum1,argNum2,argNum3]:
        if max_num<i:
            max_num=i
    return max_num
print(max_of_three(10,20,15))
