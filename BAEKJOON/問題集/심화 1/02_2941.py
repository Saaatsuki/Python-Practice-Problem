# def count_alp(argWord):
#     croa_alp = ["c=","c-","dz=","d-","lj","nj","s=","z="]
#     count = 0
#     for alp in croa_alp:
#         while alp in argWord:
#             argWord = argWord.replace(alp,"",1)
#             count += 1
    
#     argWord = argWord.replace(" ","")
#     count += len(argWord)

#     return count

# word = input().strip()
# print(count_alp(word))

def count_croatian_alphabets(word):
    croatian_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    
    for alphabet in croatian_alphabets:
        word = word.replace(alphabet, "*")
    
    print(len(word))

word = input()
count_croatian_alphabets(word)