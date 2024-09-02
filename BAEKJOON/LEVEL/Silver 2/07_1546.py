N = int(input())

num_li = list(map(int,input().split()))
li_max = max(num_li)

num_sum = 0
for num in num_li:
    num_sum += (num / li_max) * 100

print(num_sum / N)


