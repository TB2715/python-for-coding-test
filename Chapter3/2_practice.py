import random, copy


def setting():
    # N = random.randrange(2, 1001)
    # M = random.randrange(1, 10001)
    # K = random.randrange(1, M+1)

    # for testing
    N = 10
    M = 5
    K = 3
    print(f'{N}\t{M}\t{K}')

    print(f'배열의 크기: {N}')
    print(f'숫자가 더해지는 횟수: {M}')
    print(f'초과 제한: {K}')

    num_list = []
    for a_num in range(N):
        # num_list.append(random.randrange(1, 10001))
        num_list.append(random.randrange(1, 10))

    print('num_list')
    print(num_list)

    return N, M, K, num_list


if __name__ == "__main__":
    N, M, K, num_list = setting()

    prev_b_idx = 0
    is_biggest = True

    result_list = []

    for loop_count in range(M):
        biggest_num = 0
        biggest_index = 0

        if len(result_list) == M:
            break

        if is_biggest:
            for n_idx, a_num in enumerate(num_list):
                if biggest_num < a_num:
                    biggest_num = a_num
                    biggest_index = n_idx

            if M - len(result_list) < K:
                for r_count in range((M+1)-len(result_list)):
                    result_list.append((biggest_index, biggest_num))
            else:
                for r_count in range(K):
                    result_list.append((biggest_index, biggest_num))
            prev_b_idx = biggest_index
            is_biggest = False
            # Implement(result_list)

        else:
            for n_idx, a_num in enumerate(num_list):
                if n_idx == prev_b_idx:
                    continue

                if biggest_num < a_num:
                    biggest_num = a_num
                    biggest_index = n_idx

            result_list.append((biggest_index, biggest_num))
            prev_b_idx = biggest_index
            is_biggest = True
            # Implement(result_list)

    print(result_list)

    # Calcurate result
    sum = 0

    for a_result in result_list:
        index, num = a_result
        sum+=num

    print(f'Result: {sum}')
