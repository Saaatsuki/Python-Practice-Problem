count = int(input())

for _ in range(count):
    word = input()
    for idx in range(len(word)-1):
        if word[idx] == word[idx+1]:
            continue
        elif word[idx] in word[idx+1:]:
            count -= 1
            break
print(count)

# count = int(input())
# valid_count = count

# for _ in range(count):
#     word = input()
#     seen = set()
#     last_char = ""
#     is_group_word = True
    
#     for char in word:
#         if char != last_char:
#             if char in seen:
#                 is_group_word = False
#                 break
#             seen.add(char)
#         last_char = char
    
#     if not is_group_word:
#         valid_count -= 1

# print(valid_count)
