import math

prime_num_list = []
for x in range(10001):
    isPN = True
    if x < 2:
        isPN = False
    else:
        for y in range(2, int(math.sqrt(x))+1):
            if x % y == 0:
                isPN = False
                break
    prime_num_list.append(isPN)


test_count = int(input())

for _ in range(test_count):
    n = int(input())

    idx = 0
    last_pn = 0
    for idx in range(n//2, 1, -1):
        if prime_num_list[idx] and prime_num_list[n-idx]:
            print(idx, n-idx)
            break
