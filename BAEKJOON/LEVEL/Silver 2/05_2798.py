num1 , num2 = map(int,input().split())

num_li = list(map(int,input().split()))

max_sum = 0

for i in range(num1):
    for j in range(i + 1, num1):
        for k in range(j + 1, num1):
            card_sum = num_li[i] + num_li[j] + num_li[k]
            if card_sum <= num2 and card_sum > max_sum:
                max_sum = card_sum

print(max_sum)