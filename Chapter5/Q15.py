from collections import deque

N, M, K, X = map(int, input().split())
'''
N: 도시의 개수
M: 도로의 개수
K: 거리 정보
X: 출발 도시의 번호 
'''

connect_info = [[] for _ in range(M+1)]

for _ in range(M):
    start, end = map(int, input().split())

    connect_info[start].append(end)

queue = deque()
queue.append((X, 0))

distance = [-1 for _ in range(M)]

while queue:
    c_city, c_d = queue.popleft()

    for _ in connect_info[c_city]:
        pass
