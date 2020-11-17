from collections import deque


def bfs(n, m, graph):
    queue = deque([(0, 0, 1)])
    graph[0][0] = 2

    while queue:
        x, y, step = queue.popleft()

        if x == n - 1 and y == m - 1:
            return step

        if x - 1 >= 0 and graph[x - 1][y] == 1:
            queue.append((x - 1, y, step + 1))
            graph[x - 1][y] = 2
        if x + 1 < n and graph[x + 1][y] == 1:
            queue.append((x + 1, y, step + 1))
            graph[x + 1][y] = 2
        if y - 1 >= 0 and graph[x][y - 1] == 1:
            queue.append((x, y - 1, step + 1))
            graph[x][y - 1] = 2
        if y + 1 < m and graph[x][y + 1] == 1:
            queue.append((x, y + 1, step + 1))
            graph[x][y + 1] = 2


# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
n = 5
m = 6
graph = [
    [1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1]
]

print(bfs(n, m, graph))
