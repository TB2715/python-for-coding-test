def self_solution():
    current_location = input()
    x = ord(current_location[0])-96
    y = int(current_location[1])

    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    count = 0
    for idx in range(len(dx)):
        temp_x = x + dx[idx]
        temp_y = y + dy[idx]

        if 0<temp_x<8 and 0<temp_y<8:
            count += 1

    print(count)

if __name__ == '__main__':
    self_solution()
    # solution()