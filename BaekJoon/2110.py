import sys


def search_next_router(start, end):
    mid_distance = (end - start) // 2
    count = 1
    for idx, a_house in enumerate(houses[1:]):
        if (a_house - houses[idx]) > mid_distance:
            count += 1

    return count


N, C = map(int, input().split())
houses = [int(sys.stdin.readline()) for _ in range(N)].sort()

start, end = houses[0], houses[-1]

