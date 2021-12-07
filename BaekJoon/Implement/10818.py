n = int(input())

num_list = input().split()

num_list = [int(x) for x in num_list]

min = min(num_list)
max = max(num_list)

print(f'{min} {max}')