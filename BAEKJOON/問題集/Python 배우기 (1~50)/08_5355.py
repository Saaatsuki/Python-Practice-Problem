T = int(input())

for _ in range(T):
    word = input().split()

    num = float(word[0])

    for char in word[1:]:
        if char == "@":
            num *= 3
        elif char == "%":
            num += 5
        elif char == "#":
            num -= 7
    print(f"{num:.2f}")