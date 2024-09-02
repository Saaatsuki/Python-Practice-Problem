
N = int(input().strip())
string = input().strip()


r = 31
M = 1234567891


hash_value = 0
power_r = 1  

for i in range(N):
    char_value = ord(string[i]) - ord('a') + 1
    hash_value = (hash_value + char_value * power_r) % M
    power_r = (power_r * r) % M

print(hash_value)
