test_count = int(input())

for _ in range(test_count):
    hito_count = int(input())
    li_price = []
    li_name = []
    for i in range(hito_count):
        price,name = input().split()
        price_int = int(price)
        li_price.append(price_int)
        li_name.append(name)
    max_index = li_price.index(max(li_price))
    print(li_name[max_index])