import collections

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    user_input = list(map(int, input().split()))
    map_info = []
    for row in range(n):
        start = m * row
        map_info.append(user_input[start:start+m])

    for cidx in range(1, m):
        for ridx in range(n):
            pass


