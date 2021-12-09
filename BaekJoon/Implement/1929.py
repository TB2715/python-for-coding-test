import math

m, n = map(int, input().split())

for a_num in range(m, n+1):
    isPN = True
    for i in range(2, int(math.sqrt(a_num))+1):
        if a_num % i == 0:
            isPN = False
            break
    if isPN and a_num != 1:
        print(a_num)