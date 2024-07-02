

# readLine = sys.stdin.readline # 1列だけ入力をもらうことができる
# readLines = sys.stdin.readlines # Cont + Z ➡　Enter　の入力を受け取るまですべて受け取る　# リストで受け取る
# read = sys.stdin.read # Cont + Z ➡　Enter　の入力を受け取るまですべて受け取る  # ただの文字列

# result = readLines()

# result = [line.strip() for line in result]

# print(result)

# # while True:
# #     a,b = map(int,input().split())

# #     print(a+b)

import sys

input = sys.stdin.readlines

# Read lines from standard input
numberList = input()

# Process each line
for i in numberList:
    # Split each line into two numbers and convert them to integers
    a, b = map(int, i.split())
    
    # Print the sum of the two numbers
    print(a + b)