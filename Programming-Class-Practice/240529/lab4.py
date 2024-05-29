myString = "It is a great weather with you"

count = 1
for i in myString:
    if i == " ":
        count += 1
        
print(f"문자열 단어 겟수 : {count}")