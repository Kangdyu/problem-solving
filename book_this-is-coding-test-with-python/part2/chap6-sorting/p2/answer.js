const data = [
  {
    name: "홍길동",
    score: 95,
  },
  {
    name: "이순신",
    score: 77,
  },
  {
    name: "강듀",
    score: 99,
  },
  {
    name: "듀강",
    score: 44,
  },
];

function solution(data) {
  let result = [];

  data.sort((a, b) => a.score - b.score);
  result = data.map((student) => student.name);

  return result;
}

console.log(solution(data));
