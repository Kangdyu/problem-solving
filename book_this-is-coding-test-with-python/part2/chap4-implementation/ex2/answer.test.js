const solution = require("./answer");

const testCases = [
  {
    input: {
      n: 5,
    },
    output: 11475,
  },
];

describe("0204-ex2", () => {
  testCases.forEach((test, idx) => {
    const {
      input: { n },
      output,
    } = test;
    it(`${idx + 1}: n = ${n}`, () => {
      expect(solution(n)).toEqual(output);
    });
  });
});
