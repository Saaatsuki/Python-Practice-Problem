from prettytable import PrettyTable

test_di = {'Alice': 85, 'Bob': 92, 'Charlie': 88}

sorted_test_di = sorted(test_di.items(),key=lambda x:x[1],reverse=True)

table = PrettyTable([" ","name","score"])

for i ,(name,score) in enumerate(sorted_test_di,start=1):
    table.add_row([i,f'{name} 님',f"{score} 점"])

print(table)