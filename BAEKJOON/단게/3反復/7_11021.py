number = int(input())
msg = "Case #{}: {}"

for i in range(1, number + 1):
    a, b = map(int, input().split())
    sum = a + b
    print(msg.format(i, sum))
