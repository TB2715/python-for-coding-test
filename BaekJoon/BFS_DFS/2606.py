computer_count = int(input())


line_count = int(input())
connected_info = [[] for _ in range(computer_count+1)]

for _ in range(line_count):
    i, j = map(int, input().split())
    connected_info[i].append(j)
    connected_info[j].append(i)

visited = [False for _ in range(computer_count+1)]
def dfs(graph, v, visited):
    visited[v] = True
    count = 1

    for vs in graph[v]:
        if not visited[vs]:
            count += dfs(graph, vs, visited)

    return count

print(dfs(connected_info, 1, visited) - 1)