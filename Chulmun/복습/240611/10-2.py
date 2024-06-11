menu_li = ["피자","파스타","샐러드","스시","버거"]
user_sel = int(input("매뉴의 인덱스를 선택하세요 (0부터 시작) : "))
msg = f"선택된 매뉴 : {menu_li[user_sel]}" if 0<= user_sel <len(menu_li) else "유효하지 않은 선택입니다."
print(msg)