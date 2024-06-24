temp = int(input("현재 온도(섭시)를 입력하세요 : "))

sports = "수영" if 30<=temp else "등산" if 20<=temp<30 else "자전거 타기" if 10<=temp<20 else "스키"

print(f"현쟤 온도 : {temp:.1f}\n추천 활동 : {sports}")