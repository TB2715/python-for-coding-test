n, k = map(int, input('enter n, k: ').split())

count = 0
while n != 1:
    if n % k == 0:
        n = n//k
        print(f'{n*k} -> {n}')
    else:
        n -= 1
        print(f'{n+1} -> {n}')
    count += 1
print(f'count: {count}')