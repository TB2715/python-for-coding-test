from collections import deque

# input start
N, K = map(int, input().split())

map_info = []

for _ in range(N):
    map_info.append(list(map(int, input().split())))
    
S, X, Y = map(int, input().split())
# input end

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque()

for i in range(N):
    for j in range(N):
        if map_info[i][j] != 0:
            queue.append((i, j, map_info[i][j], 0))
            
sorted_queue = sorted(queue, key=lambda x: x[2])

while queue:
    v_x, v_y, v_v, time = sorted_queue.pop(0)
    
    if time == S:
        break
        
    for d_idx in range(4):
        t_x = v_x + dx[d_idx]
        t_y = v_y + dy[d_idx]
    
        if 0<=t_x<N and 0<=t_y<N:
            if map_info[t_x][t_y] == 0:
                map_info[t_x][t_y] = v_v
                sorted_queue.append((t_x, t_y, v_v, time+1))
                
print(map_info[X-1][Y-1])



## Prev code (time-out)
# for _ in range(S):
#     queue = deque()
    
#     for i in range(N):
#         for j in range(N):
#             if map_info[i][j] != 0:
#                 queue.append((i, j, map_info[i][j]))
                
#     sorted_queue = sorted(queue, key=lambda x: x[2])
    
#     while len(sorted_queue) > 0:
#         v_x, v_y, v_v = sorted_queue.pop(0)
        
#         for d_idx in range(4):
#             t_x = v_x + dx[d_idx]
#             t_y = v_y + dy[d_idx]
            
#             if t_x > -1 and t_x < N and t_y > -1 and t_y < N:
#                 if map_info[t_x][t_y] == 0:
#                     map_info[t_x][t_y] = v_v
                    
# print(map_info[X-1][Y-1])