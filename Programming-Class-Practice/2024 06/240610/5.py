def evenOdd(argNum):
    msg = "odd" if argNum%2==0 else "even"
    return msg

num = int(input("정수를 입력해!! : "))
print(evenOdd(num))