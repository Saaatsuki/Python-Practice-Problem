num1, num2, num3 = map(int,input().split())

maximum = max(num1, num2, num3)

if num1 == maximum:
    print(min(num2, num3), max(num2, num3), num1)
elif num2 == maximum:
    print(min(num1, num3), max(num1, num3), num2)
else:
    print(min(num1, num2), max(num1, num2), num3)