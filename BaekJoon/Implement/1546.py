major_num = int(input())

score_list = input().split()
score_list = [int(x) for x in score_list]

max_score = max(score_list)

new_score = []
for a_score in score_list:
    new_score.append(a_score/max_score*100)

print(sum(new_score) / major_num)