coins = [500, 100, 50, 10]
count = 0


# left = int(input('잔돈을 입력하세요: '))
left = 1260

for c in coins:
    if c/left != 0:
        this_coin_count = left//c
        print(f'{c}: {this_coin_count}개')
        count += this_coin_count
        left -= c*(left//c)
        print(f'남은 거스름돈: {left}')

print(f'전체 사용 동전 수: {count}')
