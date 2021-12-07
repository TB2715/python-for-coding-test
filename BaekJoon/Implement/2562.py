num_list = []

for _ in range(9):
    num_list.append(int(input()))

max = max(num_list)
print(f'{max}\n{num_list.index(max)+1}')