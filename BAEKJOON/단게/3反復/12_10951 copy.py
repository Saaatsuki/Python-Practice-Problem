import sys

input = sys.stdin.readlines
numberList = input()

for i in numberList:
    a,b = map(int,i.split())
    print(a+b)