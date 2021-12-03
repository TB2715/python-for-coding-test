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


if __name__ == '__main__':
    self_solution()



