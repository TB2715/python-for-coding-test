def solution():
    num_of_people = int(input())
    take_time = input().split()

    time_spend_list = [[0]*2 for _ in range(num_of_people)]
    for ps_idx in range(num_of_people):
        time_spend_list[ps_idx][0] = ps_idx
        time_spend_list[ps_idx][1] = int(take_time[ps_idx])

    time_spend_list.sort(key=lambda x: x[1])

    wait_time = 0
    wait_time_list = []
    for ps in time_spend_list:
        wait_time_list.append(wait_time + ps[1])
        wait_time += ps[1]

    print(sum(wait_time_list))


if __name__ == '__main__':
    solution()