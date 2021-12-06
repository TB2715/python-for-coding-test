def self_solution():
    map_x, map_y = map(int, input('enter x, y: ').split())
    user_x, user_y, user_direction = map(int, input('enter user x, y, direction: ').split())

    ud_list = [x for x in range(4)]
    moving_list = [(0,1), (1, 0), (0,-1), (-1,0)]

    map_info = []
    for y_idx in range(map_y):
        map_a_line = input(f'line {y_idx}: ').split()
        map_a_line = [int(x) for x in map_a_line]
        map_info.append(map_a_line)


    count = 0
    while True:
        prev_direction = user_direction
        is_moving = False

        for d_idx in range(1, 4):
            user_direction = ud_list[user_direction-d_idx]

            next_x = user_x + moving_list[user_direction][0]
            next_y = user_y + moving_list[user_direction][1]


            if map_info[next_x-1][next_y-1] == 1 and 0<next_x<map_x+1 and 0<next_y<map_y+1:
                map_info[next_x][next_y] = -1
                user_x = next_x
                user_y = next_y
                is_moving = True
                count += 1

            else:  # 바다(0)이거나, 이미 지나간 곳(-1)일 경우
                continue

        if not is_moving:
            user_direction = prev_direction

            next_x = user_x + moving_list[user_direction-2][0]
            next_y = user_y + moving_list[user_direction-2][1]

            if map_info[next_x][next_y] != 0:
                user_x = next_x
                user_y = next_y

                if map_info[next_x][next_y] != -1:
                    map_info[next_x][next_y] = -1
                    count += 1

            else: # if 뒤가 바다일 경우
                print(f'count : {count}')
                break


'''
리스트 컴프리헨션: 리스트를 초기화하는 방법 중 하나
array = [i for i in range(20) if i%2 == 1]

# N * M 크기의 2차원 리스트를 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
'''

# 왼쪽으로 회전
def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction


def solution():
    n, m = map(int, input().split())

    # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
    d = [[0] * m for _ in range(n)]

    # 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받음
    x, y, direction = map(int, input().split())
    d[x][y] = 1 # 현재 좌표 방문 처리

    # 전체 맵 정보를 입력 받음
    array = []
    for i in range(n):
        array.append(list(map(int, input().split())))

    # 북, 동, 남, 서 방향 정의
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]


    # 시뮬레이션 시작
    count = 1
    turn_time = 0
    while True:
        # 왼쪽으로 회전
        direction = turn_left(direction)
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
        if d[nx][ny] == 0 and array[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue

        # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
        else:
            turn_time += 1

        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]

            # 뒤로 갈 수 있다면 이동
            if array[nx][ny] == 0:
                x = nx
                y = ny

            # 뒤가 바다로 막힌 경우
            else:
                break
            turn_time = 0

    print(count)

if __name__ == '__main__':
    # self_solution()
    solution()