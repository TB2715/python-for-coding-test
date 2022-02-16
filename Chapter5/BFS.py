from collections import deque

def bfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')

    connected_list = deque(graph[start])
    while len(connected_list) > 0:
        c_v = connected_list.popleft()
        print(c_v, end=' ')

        temp = graph[c_v]
        for i in graph[c_v]:
            if not visited[i]:
                connected_list.append(i)
                visited[i] = True


def answer_bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)
bfs(graph, 1, visited)

print(f'\nAnswer')
visited = [False] * len(graph)
answer_bfs(graph, 1, visited)