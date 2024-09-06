N , K = map(int,input().split())

N_kake = 1
for num in range(1,N+1):
    N_kake *= num

K_kake = 1
for num in range(1,K+1):
    K_kake *= num

S = N-K
S_kake = 1
for num in range(1,S+1):
    S_kake *= num

ans = N_kake / (K_kake * S_kake)

print(ans)