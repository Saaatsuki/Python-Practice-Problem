word = input()

len_word = len(word)

while not (2<=len_word<=15):
    word = input()
    
time = 0


for i in range(len_word):
    if word[i] == "A" or word[i] == "B" or word[i] == "C":
        time += 3
    elif word[i] == "D" or word[i] == "E" or word[i] == "F":
        time += 4
    elif word[i] == "G" or word[i] == "H" or word[i] == "I":
        time += 5
    elif word[i] == "J" or word[i] == "K" or word[i] == "L":
        time += 6
    elif word[i] == "M" or word[i] == "N" or word[i] == "O":
        time += 7
    elif word[i] == "P" or word[i] == "Q" or word[i] == "R" or word[i] == "S":
        time += 8
    elif word[i] == "T" or word[i] == "U" or word[i] == "V":
        time += 9
    elif word[i] == "W" or word[i] == "X" or word[i] == "Y" or word[i] == "Z" :
        time += 10
        
# for i in range(len_word):
#     if word[i] in ["A", "B", "C"]:
#         time += 1
#     elif word[i] in ["D", "E", "F"]:
#         time += 2
#     elif word[i] in ["G", "H", "I"]:
#         time += 3
#     elif word[i] in ["J", "K", "L"]:
#         time += 4
#     elif word[i] in ["M", "N", "O"]:
#         time += 5
#     elif word[i] in ["P", "Q", "R", "S"]:
#         time += 6
#     elif word[i] in ["T", "U", "V"]:
#         time += 7
#     elif word[i] in ["W", "X", "Y", "Z"]:
#         time += 8        

        
print(time)