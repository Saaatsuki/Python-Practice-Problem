count = int(input())

for _ in range(count):
    num, txt = input().split()
    for char in txt:
        print(int(num) * char, end='')
    print()