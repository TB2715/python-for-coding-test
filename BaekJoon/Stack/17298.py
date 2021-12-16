def first_solution():
    len_a = int(input())
    a_list = list(input().split())
    a_list = [int(x) for x in a_list]

    result_list = []
    for x_idx in range(len_a-1):
        a_i = a_list[x_idx]
        max_right = max(a_list[x_idx + 1:])

        if a_i >= max_right:
            result_list.append('-1')
            continue

        else:
            for y in a_list[x_idx+1:]:
                if a_i < y:
                    result_list.append(str(y))
                    break

    result_list.append(str(-1))

    print(' '.join(result_list))

import sys


def second_solution():
    n = int(input())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    answer = [-1] * n
    queue = [(0, A[0])]

    for i in range(1, n):
        while queue[-1][1] < A[i]:
            index, num = queue.pop()
            answer[index] = A[i]

            if len(queue) == 0:
                break

        queue.append((i, A[i]))

    print(' '.join([str(x) for x in answer]))


if __name__ == '__main__':
    second_solution()
