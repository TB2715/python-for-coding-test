def recursive(k , n):
    result = 0
    if k > 0:
        for n_idx in range(1, n+1):
            result += recursive(k-1, n_idx)
        return result
    else: # if k == 0
        return n


if __name__ == '__main__':
    test_count = int(input())

    for _ in range(test_count):
        k = int(input())
        n = int(input())

        floor_list = []

        for k_idx in range(k+1):
            a_floor = []
            for n_idx in range(1, n+1):
                if k_idx == 0:
                    a_floor.append(n_idx)
                else:
                    a_floor.append(sum(floor_list[k_idx-1][:n_idx]))
            floor_list.append(a_floor)

        print(floor_list[k][n-1])