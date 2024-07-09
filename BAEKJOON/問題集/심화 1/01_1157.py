word = input().upper()
word_li = list(set(word))
li = []
for i in word_li:
    count = word.count(i)
    li.append(count)

if li.count(max(li))>=2:
    print("?")
else:
    print(word_li[li.index(max(li))])