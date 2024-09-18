def print_star(n, x=0, y=0):
    if n == 1:
        print('*', end='')
        return

    if (x // (n // 3)) % 3 == 1 and (y // (n // 3)) % 3 == 1:
        print(' ', end='')
    else:
        print('*', end='')
        

    if y == n - 1:
        print()
        y = 0
        x += 1
    else:
        y += 1

    if x < n:
        print_star(n, x, y)


N = int(input())

print_star(N)
