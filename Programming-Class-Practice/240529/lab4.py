myString = "It is a great weather with you"

count = 1
for i in myString:
    if i == " ":
        count += 1
        
print(f"문자열 단어 겟수 : {count}")

########################################################

myString = "It is a great weather with you"

str_list = list(myString.split())

print("문자열 단어 갯수: ", len(str_list))