txt = input().upper() 

li = [] 
for i in txt:
    li.append(txt.count(i))


max_count = max(li)

if li.count(max_count) >= 2:
    print("?")
else:
    max_char = txt[li.index(max_count)]
    print(max_char)
