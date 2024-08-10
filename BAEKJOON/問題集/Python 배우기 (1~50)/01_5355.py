
T = int(input())


for _ in range(T):

    word = input().split()
    

    result = float(word[0])
    

    for char in word[1:]:
        if char == '@':
            result *= 3
        elif char == '%':
            result += 5
        elif char == '#':
            result -= 7

    print(f"{result:.2f}")
