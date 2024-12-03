def getAvgSum(argNum1, argNum2):
    sum = argNum1 + argNum2
    avg = sum / 2
    return sum, avg

sum_result, avg_result = getAvgSum(10, 20)

print(f"Sum: {sum_result}")
print(f"Average: {avg_result}")
