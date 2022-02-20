n, m = map(int, input().split())

c_r, c_c, c_d = map(int, input().split()) # (1,1)에 북쪽(0)을 바라보고 서 있는 캐릭터

# for indexing 
c_r -= 1 
c_c -= 1

map_info = []
for _ in range(n):
    map_info.append(map(int, input().split()))
    
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

move_count = 0

while True:
    temp_c_d = c_d
    isMoved = False
    
    for dir in range(4):
        # 현재 방향을 기준으로 왼쪽 방향부터 찾음 
        temp_c_d = temp_c_d + 1 if (temp_c_d + 1) < 4 else 0
        
        temp_r = c_r + dx[temp_c_d]
        temp_c = c_c + dy[temp_c_d]
        
        if temp_r > -1 and temp_r < n and temp_c > -1 and temp_c < m:
            
            if map_info[temp_r][temp_c] == 0:
                c_r = temp_r
                c_c = temp_c
                c_d = temp_c_d
                isMoved = True
                break
        
            else:
                continue
            
    if isMoved == False:
        if map_info[c_r + dx[c_d - 2]][c_c + dy[c_d - 2]] != 0:
            break 
        
        else: 
            c_r = c_r + dx[c_d - 2]
            c_c = c_c + dy[c_d - 2]
            
    
        