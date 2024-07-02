import sys

# 最初に入力される数を取得
inp = int(input())

input = sys.stdin.readline

for i in range(inp):
    a, b = map(int, input().split())
    print(a + b)
