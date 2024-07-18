products = {
    'Apple': 1200,
    'Banana': 800,
    'Cherry': 1500,
    'Date': 600,
    'Elderberry': 900
}

sorted_products = sorted(products.items(),key=lambda x:x[1],reverse=False)

# for ranking,(name , val ) in enumerate(sorted_products,start=1):
#     if val<=1000:
#         print(f"{ranking:2d} : {name} ▶▷▶ {val}")

# 価格が1000円以下の商品の名前と価格を出力
affordable_products = [(name, price) for name, price in sorted_products if price <= 1000]

for name, price in affordable_products:
    print(f"{name}: {price}")
