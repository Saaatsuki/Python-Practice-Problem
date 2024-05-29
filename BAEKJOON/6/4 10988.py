word= input()

if word[::-1]==word[::1]:
    print(1)
else:
    print(0)
    
print(1) if word[::-1]==word[::1] else print(0)
    
# print(word[::-1])
# print(word[::1])

# isOkay = True
# for i in range(len(word) // 2):
#     if word[i] != word[-i -1]:
#         isOkay = False
        
# print(1) if isOkay else print(0)