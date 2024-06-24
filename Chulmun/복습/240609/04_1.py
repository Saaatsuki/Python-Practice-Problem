# 사용자로부터 초기 자본금, 구매 가격, 구매할 주식 수, 판매할 때의 주식 가격을 입력받습니다.
initial_capital = float(input("초기 자본금을 입력하세요: "))
purchase_price = float(input("주식의 구매 가격을 입력하세요: "))
purchase_quantity = int(input("구매할 주식의 수를 입력하세요: "))
selling_price = float(input("판매할 때의 주식 가격을 입력하세요: "))

# 주식 구매 비용 계산
total_purchase_cost = purchase_price * purchase_quantity

# 남은 자본금 계산
remaining_capital = initial_capital - total_purchase_cost

# 판매 예상 이익 계산
total_selling_amount = selling_price * purchase_quantity
expected_profit_or_loss = total_selling_amount - total_purchase_cost

# 결과 출력
print(f"주식 구매 후 남은 자본금: {remaining_capital:.2f}")
if expected_profit_or_loss >= 0:
    print(f"예상 이익: {expected_profit_or_loss:.2f} (예상되는 이익입니다.)")
else:
    print(f"예상 손실: {abs(expected_profit_or_loss):.2f} (예상되는 손실입니다.)")
