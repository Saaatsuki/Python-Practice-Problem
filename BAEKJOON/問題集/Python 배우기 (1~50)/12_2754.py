result = input()

num1 = 0.0
num2 = 0.0

if result == "F":
    num_sum = 0.0
else:
    if "A" in result:
        num1 = 4.0
    elif "B" in result:
        num2 = 3.0
    elif "C" in result:
        num1 = 2.0
    elif "D" in result:
        num1 = 1.0

if "+" in result:
    num2 = 0.3
elif "0" in result:
    num2 = 0.0
elif "-" in result:
    num2 = -0.3

num_sum = num1 + num2

print(num_sum)