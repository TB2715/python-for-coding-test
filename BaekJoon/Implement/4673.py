from tqdm import tqdm

num_list = [str(x) for x in range(1, 10001)]
removed_set = set()


for a_num in tqdm(range(1, 10001), desc='num list'):

    if a_num in removed_set:
        continue

    sum_num = a_num
    while sum_num < 10001:
        temp = [int(str(sum_num)[i]) for i in range(len(str(sum_num)))]
        sum_num += sum(temp)

        if sum_num < 10001:
            removed_set.add(sum_num)

for rn in removed_set:
    num_list.remove(str(rn))

for n in num_list:
    print(int(n))