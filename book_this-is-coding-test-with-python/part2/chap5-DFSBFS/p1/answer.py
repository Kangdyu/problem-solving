# Idea: 데이터를 받아 데이터를 인접 리스트로 변환한 뒤,
# 각 방문하지 않은 노드들에 대해 bfs를 돌려 체크 (bfs 횟수 = 그래프 덩어리 개수)
# Note: 너무 복잡하게 생각했다 ㅠㅠ
from collections import deque


def bfs(visited, v, graph):
    queue = deque([v])
    visited[v] = True

    while queue:
        popped = queue.popleft()

        for node in graph[popped]:
            if visited[node] is False:
                queue.append(node)
                visited[node] = True


# n, m = map(int, input().split())
# data = []
# for i in range(n):
#     data.append(list(map(int, input())))

# n = 4
# m = 5
# data = [
#     [0, 0, 1, 1, 0],
#     [0, 0, 0, 1, 1],
#     [1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0]
# ]
n = 15
m = 14
data = [
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
]

graph = dict()
visited = dict()

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            continue
        adjacent = []
        # check up
        if (i - 1 >= 0 and data[i - 1][j] == 0):
            adjacent.append(m * (i - 1) + j)
        # check left
        if (j - 1 >= 0 and data[i][j - 1] == 0):
            adjacent.append(m * i + j - 1)
        # check right
        if (j + 1 < m and data[i][j + 1] == 0):
            adjacent.append(m * i + j + 1)
        # check down
        if (i + 1 < n and data[i + 1][j] == 0):
            adjacent.append(m * (i + 1) + j)
        graph[m * i + j] = adjacent
        visited[m * i + j] = False

graph_count = 0
for key in visited.keys():
    if visited[key] is False:
        graph_count += 1
        bfs(visited, key, graph)

print(graph_count)
