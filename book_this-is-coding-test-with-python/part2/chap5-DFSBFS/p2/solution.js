class Queue {
  data = [];
  head = 0;

  constructor(datas = []) {
    this.data.push(...datas);
  }

  enqueue(data) {
    this.data.push(data);
  }

  dequeue() {
    if (this.isEmpty()) {
      throw new Error("queue is empty");
    } else {
      return this.data[this.head++];
    }
  }

  isEmpty() {
    if (this.data.length > this.head) return false;
    else return true;
  }
}

const n = 5;
const m = 6;
const graph = [
  [1, 0, 1, 0, 1, 0],
  [1, 1, 1, 1, 1, 1],
  [0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1],
];

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

function bfs(x, y) {
  const queue = new Queue();
  queue.enqueue({ x, y });

  while (!queue.isEmpty()) {
    const { x, y } = queue.dequeue();

    for (const i of [0, 1, 2, 3]) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

      if (graph[nx][ny] === 1) {
        graph[nx][ny] = graph[x][y] + 1;
        queue.enqueue({ x: nx, y: ny });
      }
    }
  }

  return graph[n - 1][m - 1];
}

function solution() {
  return bfs(0, 0);
}

console.log(solution());
