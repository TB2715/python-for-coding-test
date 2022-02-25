import sys

N = int(input())

home_list = list(map(int, input().split()))
distance_list = []

for th in home_list:
    sum = 0
    for ah in home_list:
        sum += abs(ah-th)
    distance_list.append((sum, th))

distance_list.sort(key=lambda x: (x[0], x[1]))

# print(f"idx: {distance_list[0][1]}, sum:{distance_list[0][0]}")
print(distance_list[0][1])


N = int(input())

home_list = list(map(int, input().split()))
home_list.sort()

print(home_list[(N-1)//2])
# 홀수일 경우 무조건 중간값이
# 짝수일 경우, 중간을 기준으로 좌우값의 거리차 합이 동일하므로 왼쪽 집 선택
