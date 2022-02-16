n, m = map(int, input().split())
board_list = []

for _ in range(n):
    board_list.append(input())

count_list = []

for n_idx in range(n-7):
    for m_idx in range(m-7):
        start_w = 0 # 'W'로 시작하는 경우에 바뀐 체스판의 갯수를 세기 위함
        start_b = 0 # 'B'로 시작하는 경우에 바뀐 체스판의 갯수를 세기 위함

        for x in range(n_idx, n_idx+8):
            for y in range(m_idx, m_idx+8):
                if (x+y)%2 == 0:
                    # 좌표값의 합이 2의 배수라면 (0,0)의 index의 색과 같아야함.
                    if board_list[x][y] != 'W': # (0,0)의 색이 W일 때, [i][j]의 색이 W가 아닐 경우 변경해야함
                        start_w += 1
                    if board_list[x][y] != 'B': # (0,0)의 색이 B일 때, [i][j]의 색이 B가 아닐 경우 변경해야함
                        start_b += 1
                else:
                    if board_list[x][y] != 'B':
                        start_w += 1
                    if board_list[x][y] != 'W':
                        start_b += 1
        count_list.append(min(start_w, start_b))

print(min(count_list))
