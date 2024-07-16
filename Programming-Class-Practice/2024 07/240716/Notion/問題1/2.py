products = {
    'Apple': 1200,
    'Banana': 800,
    'Cherry': 1500,
    'Date': 600,
    'Elderberry': 900
}

sorted_products = sorted(products.items(),key=lambda x:x[1],reverse=False)

for ranking,(name , val ) in enumerate(sorted_products,start=1):
    if val<=1000:
        print(f"{ranking:2d} : {name} ▶▷▶ {val}")