N, M = map(int, input().split())

map_info = []

for _ in N:
    map_info.append(list(map(int, input().split()))) 

test_map = [ [0] * M for _ in range(N) ]

# Four direction
dx = [-1, 1, 0, 0] # left, right, down, up
dy = [0, 0, -1, 1]

result = 0

# DFS를 통해 경우의 수를 구함 
def infection(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 각 방향에서 바이러스가 퍼질 수 있는 경우 
        if nx >= 0 and nx<N and ny>=0 and ny<M:
            if test_map[nx][ny] == 0:
                # 해당 위치에 바이러스를 배치 후 재귀적으로 수행 
                test_map[nx][ny] = 2
                infection(nx, ny)
                

# 현재 맵에서 안전 영역의 크기를 계산하는 함수             
def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if test_map[i][j] == 0:
                score += 1
    
    return score 

# 깊이 우선 탐색(DFS_BFS)를 이용해 울타리를 설치하면서, 매번 안전 영역의 크기를 계산함
def dfs(count):
    global result 
    
    # 울타리가 3개 설치 완료된 경우 
    if count == 3:
        for i in range(n):
            for j in range(m):
                test_map[i][j] = map_info[i][j]
                
        # 각 바이러스의 위치에서 전파 진행 
        for i in range(n):
            for j in range(m):
                # if test_map[i][j] = map_info[]
                pass
    