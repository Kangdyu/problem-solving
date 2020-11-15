const solution = require("./answer");

const testCases = [
  {
    input: {
      n: 1260,
    },
    output: 6,
  },
  {
    input: {
      n: 570,
    },
    output: 4,
  },
];

describe("test", () => {
  testCases.forEach((test, idx) => {
    const {
      input: { n },
      output,
    } = test;
    it(`${idx + 1}: n = ${n}`, () => {
      expect(solution(n)).toBe(output);
    });
  });
});
