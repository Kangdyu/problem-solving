const INF = 1000000000;
const n = 6;
const m = 11;
const start = 1;
const graph = [
  [],
  [
    [2, 2],
    [3, 5],
    [4, 1],
  ],
  [
    [3, 3],
    [4, 2],
  ],
  [
    [2, 3],
    [6, 5],
  ],
  [
    [3, 3],
    [5, 1],
  ],
  [
    [3, 1],
    [6, 2],
  ],
  [],
];
const visited = new Array(n + 1).fill(false);
const distance = new Array(n + 1).fill(INF);

function getSmallestNode() {
  let minValue = INF;
  let index = 0;

  for (let i = 1; i <= n; i++) {
    if (visited[i] === false && distance[i] < minValue) {
      minValue = distance[i];
      index = i;
    }
  }

  return index;
}

function dijkstra(start) {
  distance[start] = 0;
  visited[start] = true;

  for (const adjacent of graph[start]) {
    const [node, cost] = adjacent;
    distance[node] = cost;
  }

  for (let i = 0; i < n - 1; i++) {
    const now = getSmallestNode();
    visited[now] = true;

    for (const adjacent of graph[now]) {
      const [node, cost] = adjacent;
      const totalCost = distance[now] + cost;
      if (totalCost < distance[node]) {
        distance[node] = totalCost;
      }
    }
  }
}

dijkstra(start);

for (let i = 1; i <= n; i++) {
  if (distance[i] === INF) console.log('INF ');
  else console.log(distance[i]);
}
