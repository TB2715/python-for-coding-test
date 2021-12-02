def solution():
    n, k = map(int, input('enter n, k: ').split())
    value_list = [int(input(f'enter value {idx}: ')) for idx in range(n)]

    count = 0
    for a_value in reversed(value_list):
        if k >= a_value:
            count += k // a_value
            k = k % a_value

        if k == 0:
            break

    print(count)
    return count


if __name__ == "__main__":
    answer = solution()
    print(f'answer: {answer}')