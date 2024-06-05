def maxFunction(arg_list):
    max_value = arg_list[0]
    for i in arg_list:
        if i > max_value:
            max_value = i
    return max_value
            

def minFunction(arg_list):
    min_value = arg_list[0]
    for i in arg_list:
        if i < min_value:
            min_value = i
    return min_value
            
    

example_list = [1, 3, 5, 7, 9]

result = maxFunction(example_list)
result2 = minFunction(example_list)

print(result)
print(result2)