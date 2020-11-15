const solution = require("./answer");

const testCases = [
  {
    input: {
      n: 3,
      m: 3,
      data: [
        [3, 1, 2],
        [4, 1, 4],
        [2, 2, 2],
      ],
    },
    output: 2,
  },
  {
    input: {
      n: 2,
      m: 4,
      data: [
        [7, 3, 1, 8],
        [3, 3, 3, 4],
      ],
    },
    output: 3,
  },
];

describe("test", () => {
  testCases.forEach((test, idx) => {
    const {
      input: { n, m, data },
      output,
    } = test;
    it(`${idx + 1}: n = ${n}, m = ${m}, data = ${data}`, () => {
      expect(solution(n, m, data)).toBe(output);
    });
  });
});
