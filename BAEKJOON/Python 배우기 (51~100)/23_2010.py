cou = int(input())

sum_num = 0
for _ in range(cou):
    num = int(input())
    sum_num += num

print(sum_num - (cou-1))