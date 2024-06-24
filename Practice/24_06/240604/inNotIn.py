def inFunction(arg_value, arg_list):
    for i in arg_list:
        if i == arg_value:
            return True
    return False
        
        
def notInFunction(arg_value, arg_list):
    for i in arg_list:
        if i == arg_value:
            return False
    return True


example_value = 1

example_list = [1, 3, 5, 7, 9]


result = inFunction(example_value, example_list)
result2 = notInFunction(example_value, example_list)
result3 = example_value in example_list
result4 = example_value not in example_list

print(result)
print(result2)
print(result3)
print(result4)