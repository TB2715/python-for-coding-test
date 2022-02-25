import sys

N = int(input())

s_list = []
name_list = []

for idx in range(N):
    u_input = input().split()
    name_list.append(u_input[0])

    temp_list = [idx, u_input[0].lower()]
    temp_list.extend(list(map(int, u_input[1:])))
    s_list.append(temp_list)

s_list.sort(key=lambda x: (-x[2], x[3], -x[4], x[1]))

for item in s_list:
    # print(f"{name_list[item[0]]}\t{item[2:]}")
    sys.stdout.write(f"{name_list[item[0]]}\t{item[2:]}\n")