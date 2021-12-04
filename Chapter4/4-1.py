def self_solution():
    n = int(input())
    move_list = input().split()

    current_location = [1, 1]

    for a_move in move_list:
        if a_move == 'D':
            if current_location[0] == n:
                continue
            else:
                current_location[0] += 1
        elif a_move == 'U':
            if current_location[0] == 1:
                continue
            else:
                current_location[0] -= 1
        elif a_move == 'R':
            if current_location[1] == n:
                continue
            else:
                current_location[1] += 1
        elif a_move == 'L':
            if current_location[1] == 1:
                continue
            else:
                current_location[1] -= 1

    print(f'{current_location[0]} {current_location[1]}')


def solution():
    n = int(input())
    x, y = 1, 1
    plans = input().split()

    # L, R, U, D에 따른 이동 방향
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    # 이동 계획을 하나씩 확인
    for plan in plans:
        # 이동 후 좌표 구하기
        for i in range(len(move_types)): # 4가지 경우 중 해당되는 i에 대해 확인
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]

        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        # 이동 수행
        x, y = nx, ny

    print(x, y)

if __name__ == '__main__':
    # self_solution()
    solution()



