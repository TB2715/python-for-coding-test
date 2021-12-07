han = [x for x in range(1, 100)] # 2자리수까지는 다 한수이다

for x in range(100, 1001):
    str_x = str(x)

    is_han = True
    prev_diff = int(str_x[0]) - int(str_x[1])
    for x_idx in range(1, len(str_x) - 1):
        first = str_x[x_idx]
        second = str_x[x_idx + 1]
        temp_diff = int(first) - int(second)

        if prev_diff != temp_diff:
            is_han = False
            break

    if is_han:
        han.append(x)

n = int(input())
if n >= han[-1]:
    print(len(han))
else:
    for ah_idx, a_han in enumerate(han):
        if a_han > n:
            print(ah_idx)
            break
