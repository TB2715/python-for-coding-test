from collections import deque
import queue

N, K = map(int, input().split())
map_list = []
virus_list = []

for i in range(N):
    map_list.append(list(map(int, input().split())))
    
    for j in range(N):
        if map_list[i][j] != 0:
            virus_list.append((map_list[i][j], i, j, 0))
            
S, X, Y = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

virus_list.sort()
q = deque(virus_list)

while q:
    v_v, v_x, v_y, time = q.popleft()
    
    if time == S:
        break
    
    for i in range(4):
        n_x = v_x + dx[i]
        n_y = v_y + dy[i]
        
        if 0<= n_x < N and 0 <= n_y < N:
            if map_list[n_x][n_y] == 0:
                map_list[n_x][n_y] = v_v
                q.append((v_v, n_x, n_y, time+1))
                
print(map_list[X-1][Y-1])