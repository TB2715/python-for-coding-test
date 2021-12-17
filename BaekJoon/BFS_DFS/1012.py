# from collections import deque
#
# test_count = int(input())
#
# for _ in range(test_count):
#     M, N, K = map(int, input().split())
#     connected = [[0]*M for _ in range(N)]
#
#     for _ in range(K):
#         temp_m, temp_n = map(int, input().split())
#         connected[temp_n][temp_m] = 1
#
#     dm = [-1, 1, 0, 0]
#     dn = [0, 0, -1, 1]
#
#     def bfs(connected, v):
#         cn, cm = v
#         queue = deque([(cn, cm)])
#         connected[cn][cm] = 0
#
#         while queue:
#             cn, cm = queue.popleft()
#
#             for i in range(4):
#                 nm = cm + dm[i]
#                 nn = cn + dn[i]
#
#                 if nm < 0 or nm > M-1 or nn < 0 or nm > N-1:
#                     continue
#                 else:
#                     if connected[nn][nm] == 1:
#                         queue.append((nn, nm))
#                         connected[nn][nm] = 0
#
#
#     result = 0
#     for a_n in range(N):
#         for a_m in range(M):
#             if connected[a_n][a_m] == 1:
#                 result += 1
#                 bfs(connected, (a_n, a_m))
#
#     print(result)


import sys

def dfs(field, v_info, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = v_info[0] + dx[i]
        ny = v_info[1] + dy[i]

        if nx < 0 or nx >= M or ny<0 or ny>= N:
            continue

        else:
            if field[ny][nx] == 1:
                field[ny][nx] = 0
                dfs(field, (nx, ny), N, M)


if __name__=='__main__':
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        field = [[0] * M for _ in range(N)]

        count = 0

        for _ in range(K):
            temp_x, temp_y = map(int, input().split())
            field[temp_y][temp_x] = 1

        for axis_y in range(N):
            for axis_x in range(M):
                if field[axis_y][axis_x] == 1:
                    field[axis_y][axis_x] = 0
                    count += 1
                    dfs(field, (axis_x, axis_y), N, M)

        print(count)
