import random

def setting():

    row, col = map(int, input('enter row, col: ').split())

    num_list = []
    for r in range(row):
        col_list = []
        for c in range(col):
            col_list.append(random.randrange(1, 11))
        print(col_list)
        num_list.append(col_list)
    return num_list


if __name__ == '__main__':
    num_list = setting()

    min = []
    for a_row in num_list:

        temp_min = 10001
        for a_num in a_row:
            if a_num < temp_min:
                temp_min = a_num
        min.append(temp_min)
    min = sorted(min)

    print(f'각 열에서 가장 작은 수 중에서 큰 수는 {min[-1]}이다.')

