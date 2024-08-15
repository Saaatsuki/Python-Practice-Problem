T1 = int(input())

for _ in range(T1):
    T2 = int(input())
    num_li = list(map(int,input().split()))
    print(2 * (max(num_li)-min(num_li)))