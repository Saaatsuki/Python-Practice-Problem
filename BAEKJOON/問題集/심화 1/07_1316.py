count = int(input())


for _ in range(count):
    word = input()
    for idx in range(len(word)-1):
        if word[idx] == word[idx+1]:
            continue
        elif word[idx] in word[idx+1:]:
            count -= 1
print(count)