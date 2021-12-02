def how_to_use_sort_lambda():
    test_list = [(1,2), (0,1), (5,2), (5,1), (3,0)]
    print(test_list)

    # 그냥 sorted 사용 시, 리스트 아이템의 각 요소 순서대로 정렬함
    print(sorted(test_list))
    # [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

    # key 인자에 함수를 넘겨주면, 해당 함수릐 반환값을 비교하여 순서대로 정렬
    print('sorted by first value')
    print(sorted(test_list, key=lambda x: x[0]))
    # [(0, 1), (1, 2), (3, 0), (5, 2), (5, 1)]

    print('sorted by second value')
    print(sorted(test_list, key=lambda x: x[1]))
    # [(3, 0), (0, 1), (5, 1), (1, 2), (5, 2)]

    # 아이템 첫 번째 value를 기준으로 오름차준으로 정렬 후, 그 사이에 두 번째 value를 기준으로 "내림차순"으로 정렬 시
    test_list2 = [(1, 2), (0, 3), (0, 1), (1, 3), (1, 0), (2, 1)]
    print(sorted(test_list2, key= lambda x : (x[0], -x[1])))
    # [(0, 3), (0, 1), (1, 3), (1, 2), (1, 0), (2, 1)]


def solution():
    n = int(input())

    time = [[0]*2 for _ in range(n)]
    for i in range(n):
        start, end = map(int, input().split())
        time[i][0] = start
        time[i][1] = end

    # sorted_value_list = sorted(time, key=lambda x: (x[1], x[0]))
    time.sort(key= lambda x: (x[1], x[0]))

    count = 1
    end_time = time[0][1]
    for t_idx in range(1, n):
        if time[t_idx][0] >= end_time:
            end_time = time[t_idx][1]
            count += 1

    print(count)




if __name__ == '__main__':
    # how_to_use_sort_lambda()
    solution()