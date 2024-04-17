# 初期資本
Initial_capital = float(input("Please enter initial capital🥚："))
# 株一つの購入金額
Purchase_price_of_shares = float(input("Please enter Purchase price of shares🐣："))
# 購入する株数
Number_of_shares_to_buy = float(input("Please enter Number of shares to buy🐥："))
# 売却時の株価
Stock_price_at_the_time_of_sale = float(input("Please enter Stock price at the time of sale🐓："))


# 株購入費用の計算(購入価格と株数を掛けて、総購入費用を計算)
total_price_of_a_stock_purchased = Purchase_price_of_shares * Number_of_shares_to_buy

# 資本金残高
remaining_capital = Initial_capital - total_price_of_a_stock_purchased

# 売却予想利益の計算(売却時の株価と株数を掛けて総売却額を計算➡総購入費用を引いて、予想利益または損失を計算)
estimated_profit_from_the_sale = (Stock_price_at_the_time_of_sale * Number_of_shares_to_buy) - total_price_of_a_stock_purchased 


print("post-purchase capital💰：",remaining_capital)
print("anticipated profit💰：",estimated_profit_from_the_sale)

if (estimated_profit_from_the_sale > 0):
    print("It's expected profit.(❁´◡`❁)")
elif (estimated_profit_from_the_sale < 0):
    print("It's an expected loss.(ToT)/~~~")
else:
    print("There is no loss or profit🐼")
