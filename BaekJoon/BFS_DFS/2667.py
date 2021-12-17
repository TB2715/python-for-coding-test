n = int(input())

# map_list = [[] for _ in range(n)]
map_list = []
for _ in range(n):
    map_list.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dps(map_list, v):
    cx, cy = v
    map_list[cx][cy] = 0
    count = 1

    for d in range(4):
        nx = cx + dx[d]
        ny = cy + dy[d]

        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
            continue
        else:
            if map_list[nx][ny] == 1:
                count += dps(map_list, (nx, ny))

    return count

count_list = []
for i in range(n):
    for j in range(n):
        if map_list[i][j] == 1:
            count_list.append(dps(map_list, (i, j)))

print(len(count_list))
print('\n'.join([str(x) for x in sorted(count_list)]))

