li = []
for i in range(8):
    num = int(input())
    li.append((num, i + 1)) 

li_sorted = sorted(li, reverse=True, key=lambda x: x[0])

top_5 = li_sorted[:5]
total_score = sum(x[0] for x in top_5)
top_5_indices = sorted(x[1] for x in top_5)

print(total_score)
print(" ".join(map(str, top_5_indices)))
