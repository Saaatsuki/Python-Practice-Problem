tenp = int(input("현재 온도(섭씨) 입력하세요:"))

msg = "수영" if tenp >= 30 else "등산" if tenp >= 20 else "자전거 타기" if tenp >= 10 else "스키"

# if 30<=tenp :
#     msg = "수영"
# elif 20<=tenp<30:
#     msg = "등산"
# elif 10<=tenp<20:
#     msg = "자전거 타기"
# else:
#     msg = "스키"

print(f"현재 온도 : {tenp}\n추천 활동 : {msg}")