const solution = require("./answer");

const testCases = [
  {
    input: {
      n: 5,
      commands: ["R", "R", "R", "U", "D", "D"],
    },
    output: {
      x: 4,
      y: 3,
    },
  },
];

describe("0204-ex1", () => {
  testCases.forEach((test, idx) => {
    const {
      input: { n, commands },
      output,
    } = test;
    it(`${idx + 1}: n = ${n}, commands = ${commands}`, () => {
      expect(solution(n, commands)).toEqual(output);
    });
  });
});
