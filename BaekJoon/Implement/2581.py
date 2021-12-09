import math

m = int(input())
n = int(input())

prime_n = []

for a_num in range(m, n+1):
    isPN = True
    for i in range(2, int(math.sqrt(a_num))+1):
        if a_num % i == 0:
            isPN = False
            break
    if isPN and a_num != 1:
        prime_n.append(a_num)

if len(prime_n) == 0:
    print(-1)
else:
    print(sum(prime_n))
    print(min(prime_n))