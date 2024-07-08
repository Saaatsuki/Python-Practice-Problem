word = input().upper()

li = []
for i in word:
    li.append(word.count(i))
print(li)
print(word[li.index(max(li))])