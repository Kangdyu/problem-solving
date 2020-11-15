const solution = require("./answer");

const testCases = [
  {
    input: {
      n: 25,
      k: 5,
    },
    output: 2,
  },
  {
    input: {
      n: 17,
      k: 4,
    },
    output: 3,
  },
  {
    input: {
      n: 25,
      k: 3,
    },
    output: 6,
  },
];

describe("test", () => {
  testCases.forEach((test, idx) => {
    const {
      input: { n, k },
      output,
    } = test;
    it(`${idx + 1}: n = ${n}, k = ${k}`, () => {
      expect(solution(n, k)).toBe(output);
    });
  });
});
