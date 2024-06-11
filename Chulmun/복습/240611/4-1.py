first_money = int(input("조기 자본금을 입력하세요. : "))
buy_kabu_price = int(input("주식 가격을 입력하세요. : "))
kabu_count = int(input("구매할 수를 입력하세요. : "))
sell_kabu_peice = int(input("판매할 때의 주식 가격를 입력하세요. : "))

total_money = buy_kabu_price * kabu_count
rem_money = abs(total_money - first_money)
total_sell_price = sell_kabu_peice * kabu_count
son = total_sell_price - total_money

msg = "이익" if 0<=son else "손실"
print(f"구매 후 남은 자본금 : {rem_money:.2f}\n예상 이익 : {son:.2f}\n예상되는 {msg}입니다.")