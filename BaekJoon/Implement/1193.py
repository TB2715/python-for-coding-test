n = int(input())

plus = 1
prev_sum = 0
sum = 1
while True:
    if n <= sum:
        break

    else:
        plus += 1
        prev_sum = sum
        sum += plus


for i in range(1, plus+1):
    if prev_sum + i == n:
        if plus % 2 == 0:
            print(f'{i}/{plus+1-i}')
            break
        else:
            print(f'{plus+1-i}/{i}')
            break

x=2