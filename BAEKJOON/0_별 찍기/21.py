n = int(input("Enter a number for alternating lines: "))

for _ in range(n):
    print('* ' * (n - n // 2))
    print(' *' * (n // 2))
