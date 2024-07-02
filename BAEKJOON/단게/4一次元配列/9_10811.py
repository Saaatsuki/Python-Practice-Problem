import sys

input = sys.stdin.readline

n,m = map(int,input().split())

basket = list(i for i in range(n+1))

for _ in range (m):
    i,j = map(int,input().split())
    while(i<j):
        basket[i],basket[j] = basket[j],basket[i]
        i += 1
        j += 1
        
for i in range(1,1+n):
    print(basket[i],end = " ")