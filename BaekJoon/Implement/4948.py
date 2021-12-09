import math
from tqdm import tqdm

prime_num_list = []
for a_num in tqdm(range(1, 246913)):
    isPN = True
    for i in range(2, int(math.sqrt(a_num)) + 1):
        if a_num % i == 0:
            isPN = False
            break
    if isPN and a_num != 1:
        prime_num_list.append(a_num)


while True:
    n = int(input())

    if n == 0:
        break
    elif n == 1:
        print(1)
        continue

    else:
        count = 0
        for idx, a_num in enumerate(prime_num_list):
            if n < a_num <= 2*n:
                count += 1
        print(count)
