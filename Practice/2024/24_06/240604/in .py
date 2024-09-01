def isValueInList(arg_list, arg_value):
    isExist = False
    for i in arg_list:
        if i == arg_value:
            isExist = True
            break
        else:
            isExist = False
    return isExist
    
    

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample_value = 3

print(isValueInList(sample_list, sample_value))