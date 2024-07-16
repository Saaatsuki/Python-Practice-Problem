test_di = {'Alice': 85, 'Bob': 92, 'Charlie': 88}

sorted_test_di = sorted(test_di.items(),key=lambda x:x[1],reverse=False)

for i ,(name,score) in enumerate(sorted_test_di,start=1):
    print(f"{i}, {name} : {score}")