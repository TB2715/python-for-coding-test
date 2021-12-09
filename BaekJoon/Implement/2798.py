n, m = map(int, input().split())
cards = [int(x) for x in input().split()]

max_num = 0

for f_idx, first in enumerate(cards):
    for second in cards[f_idx + 1:]:
        s_idx = cards.index(second)
        for third in cards[s_idx + 1:]:
            temp_sum = first + second + third

            if max_num < temp_sum <= m:
                if temp_sum == m:
                    print(temp_sum)
                    quit()
                else:
                    max_num = temp_sum
print(max_num)
