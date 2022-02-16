from collections import deque

n, m, v = map(int, input().split())

connected_map = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    connected_map[i].append(j)
    connected_map[j].append(i)

for idx in range(len(connected_map)):
    connected_map[idx] = sorted(connected_map[idx])

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


visited = [ False for _ in range(n+1)]
dfs(connected_map, v, visited)


def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        c_v = queue.popleft()
        print(c_v, end=' ')

        for i in graph[c_v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

print('')
visited = [False for _ in range(n+1)]
bfs(connected_map, v, visited)

