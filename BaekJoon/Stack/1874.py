def first_solution():
    n = int(input())

    user_input_list = []
    for _ in range(n):
        user_input_list.append(int(input()))

    max_index = user_input_list.index(max(user_input_list))
    prev_num = n
    for temp_num in user_input_list[max_index+1:]:
        if prev_num < temp_num:
            print('NO')
            quit()
        prev_num = temp_num


    idx = 0
    num_list = []
    new_list = []
    for num in range(1, n+1):
        num_list.append(num)
        print('+')

        if num == n:
            break

        while user_input_list[len(new_list)] == num_list[-1]:
            new_list.append(num_list[-1])
            print('-')
            num_list.pop()

            if len(num_list) == 0:
                break


def second_solution():
    n = int(input())

    count = 0
    stack = []
    result = []

    for i in range(n):
        x = int(input())

        while count < x:
            count += 1
            stack.append(count)
            result.append('+')

        if stack[-1] == x:
            result.append('-')
            stack.pop()
            continue
        else:
            print('NO')
            exit()

    print('\n'.join(result))


if __name__=='__main__':
    second_solution()