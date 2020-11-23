INF = int(1e9)
# 노드 개수
n = int(input())
# 간선 개수
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    arr, dest, cost = map(int, input().split())
    graph[arr][dest] = cost


def floyd_warshall():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if j == i or k == i or j == k:
                    continue
                graph[j][k] = min(
                    graph[j][k], graph[j][i] + graph[i][k])


floyd_warshall()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        d = graph[i][j]
        if d == INF:
            print(f'{"INF":3}', end=" ")
        else:
            print(f'{d:3}', end=" ")
    print()
