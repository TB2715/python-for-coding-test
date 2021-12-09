while True:
    user_input = input().split()
    user_input = [int(x)*int(x) for x in user_input]

    if user_input[0] == 0 and user_input[1] == 0 and user_input[2] == 0:
        break

    max_len = max(user_input)
    max_idx = user_input.index(max_len)

    len_sum = 0
    for idx, x in enumerate(user_input):
        if idx == max_idx:
            continue
        else:
           len_sum += x

    print('right') if len_sum == max_len else print('wrong')