def solution(N, num_list):
    return find_fixed_point(0, len(num_list)-1, num_list)


def find_fixed_point(start, end, num_list):
    if start > end:
        return -1

    mid = (start + end) // 2
    if num_list[mid] > mid:
        return find_fixed_point(start, mid-1, num_list)
    elif num_list[mid] < mid:
        return find_fixed_point(mid+1, end, num_list)
    else:
        return mid


if __name__ == '__main__':
    # print(solution(5, [-15, -6, 1, 3, 7]))
    print(solution(7, [-15, -4, 2, 8, 9, 13, 15]))