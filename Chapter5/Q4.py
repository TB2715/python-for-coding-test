import math
n, m = map(int, input().split())

map_list = []
for _ in range(n):
    temp_input = input()
    map_list.append([int(x) for x in temp_input])


def bfs(map_list, start):
    cx, cy = start
    move_count = 1
    if cx == m-1 and cy == n-1:
        return move_count
    else:
        right = math.inf
        down = math.inf
        if cx < m-1 and map_list[cy][cx+1] != 0:
            right = bfs(map_list, (cx+1, cy))
        if cy < n-1 and map_list[cy+1][cx] != 0:
            down = bfs(map_list, (cx, cy+1))
        move_count += min(right, down)
        return move_count

print(bfs(map_list, (0,0)))

## 뭔가.. 이상함
