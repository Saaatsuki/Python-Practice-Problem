count = 0 
# 만약에 i 가 홀수이라면 skip
for i in range(1,21):
    if i%2!=0:
        continue
    count += i

# 짝수(偶数) 홀수(奇数)
print(f"1~20의 짝수 합계 (홀수 건너뜀) : {count}")