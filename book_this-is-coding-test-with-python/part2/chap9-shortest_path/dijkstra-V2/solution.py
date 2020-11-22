import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # mine
    # distance[start] = 0
    # target_node = start

    # while target_node != 0:
    #     visited[target_node] = True
    #     adjacent_nodes = graph[target_node]
    #     for node, dist in adjacent_nodes:
    #         distance[node] = min(distance[node], distance[target_node] + dist)
    #     target_node = get_smallest_node()
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]

    for _ in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost


dijkstra(start)

for i in distance[1:]:
    if i == INF:
        print("INFINITY", end=" ")
    else:
        print(i, end=" ")
