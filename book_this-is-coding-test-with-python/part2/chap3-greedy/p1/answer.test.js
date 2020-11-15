const solution = require("./answer");

const testCases = [
  {
    input: {
      n: 5,
      m: 8,
      k: 3,
      data: [2, 4, 5, 4, 6],
    },
    output: 46,
  },
  {
    input: {
      n: 5,
      m: 7,
      k: 2,
      data: [3, 4, 3, 4, 3],
    },
    output: 28,
  },
];

describe("test", () => {
  testCases.forEach((test, idx) => {
    const {
      input: { n, m, k, data },
      output,
    } = test;
    it(`${idx + 1}: n = ${n}, m = ${m}, k = ${k}, data = ${data}`, () => {
      expect(solution(n, m, k, data)).toBe(output);
    });
  });
});
