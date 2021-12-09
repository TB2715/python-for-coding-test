num_people = int(input())

people_list = []

for idx in range(num_people):
    kg, cm = map(int, input().split())
    people_list.append((kg, cm))

rank_list = []
for apidx, a_p in enumerate(people_list):
    rank = 1

    for spidx, s_p in enumerate(people_list):
        if apidx == spidx:
            continue

        # A보다 덩치(키와 무게)가 큰 사람을 만난 경우
        if a_p[0] < s_p[0] and a_p[1] < s_p[1]:
            rank += 1

    rank_list.append(str(rank))

print(' '.join(rank_list))