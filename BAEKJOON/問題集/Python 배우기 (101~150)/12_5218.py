T = int(input())

for _ in range(T):
    word1, word2 = input().split()

    li = []
    for i in range(len(word1)):
        if ord(word2[i]) >= ord(word1[i]):
            dis = ord(word2[i]) - ord(word1[i])
        else:
            dis = (ord(word2[i]) + 26) - ord(word1[i])
        
        li.append(str(dis))

    print(f"Distances: {' '.join(li)}")
