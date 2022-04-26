# import math
# from collections import deque
#
# n, m = map(int, input().split())
#
# map_list = []
# for _ in range(n):
#     temp_input = input()
#     map_list.append([int(x) for x in temp_input])
#
#
# def bfs(map_list, start):
#     # cx, cy = start
#     # move_count = 1
#     # if cx == m-1 and cy == n-1:
#     #     return move_count
#     # else:
#     #     right = math.inf
#     #     down = math.inf
#     #     if cx < m-1 and map_list[cy][cx+1] != 0:
#     #         right = bfs(map_list, (cx+1, cy))
#     #     if cy < n-1 and map_list[cy+1][cx] != 0:
#     #         down = bfs(map_list, (cx, cy+1))
#     #     move_count += min(right, down)
#     #     return move_count
#
# # print(bfs(map_list, (0, 0)))
#
# # ---- 뭔가 이상함
#
#     dn = [1, -1, 0, 0]
#     dm = [0, 0, 1, -1]
#
#     queue = deque([start])
#     while queue:
#         cn, cm = queue.popleft()
#
#         for idx in range(4):
#             nn = cn + dn[idx]
#             nm = cm + dm[idx]
#
#             if nn < 0 or nm < 0 or nn >= n or nm >= m:
#                 continue
#
#             if map_list[nn][nm] == 0:
#                 continue
#
#             if map_list[nn][nm] == 1:
#                 map_list[nn][nm] = map_list[cn][cm] + 1
#                 queue.append((nn, nm))
#
#     return map_list[n-1][m-1]
from collections import deque

N, M = map(int, input().split())

map_info = []
for _ in range(N):
    map_info.append(list(map(int, input().split())))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque((0, 0, 1))

while queue:
    cx, cy, cv = queue.popleft()

    for i in range(4):
        if map_info[dx[i]][dy[i]] != 0:
            pass

