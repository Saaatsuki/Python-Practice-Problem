def number(num1):
    if num1 > 0:
        print("正")
    elif num1 < 0:
        print("負")
    elif num1 == 0:
        print("ZERO")

num1 = int(input("Please enter a ingere : "))
number(num1)