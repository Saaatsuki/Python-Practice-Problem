star = int(input())

for i in range(star):
    print(f"{' '*i}{'*'*(star-i)}{'*'*(star-(i+1))}")