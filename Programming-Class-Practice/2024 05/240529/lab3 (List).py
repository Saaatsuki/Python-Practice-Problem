myString = "hello hyndai hoho"
# "h"만 보관하는 리스트를 설정한다
list_h = []

# 만약에 "myString"안에 "h"가 있으면 list_h로 주가
for i in myString:
    if i == "h":
        list_h.append(i)
        
print(f"문자열 내 h 곗수 : {len(list_h)}")