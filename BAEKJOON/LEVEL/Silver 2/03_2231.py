N = int(input())

def decomposition_sum(x):
    return x + sum(int(digit) for digit in str(x))

min_constructor = 0
for i in range(1, N + 1):
    if decomposition_sum(i) == N:
        min_constructor = i
        break

print(min_constructor)
