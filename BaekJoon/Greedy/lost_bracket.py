def solution():
    numbers = input()

    num_list = numbers.split('-')

    sum_list = []
    for num_group in num_list:
        temp_list = num_group.split('+')

        sum = 0
        for t in temp_list:
            sum += int(t)
        sum_list.append(sum)

    result = sum_list[0]
    for sum in sum_list[1:]:
        result -= sum

    print(result)


if __name__ == '__main__':
    solution()