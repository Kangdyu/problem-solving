// import readline from "readline";

// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });

// let lines = [];
// let lineLimit = 2;
// let curLine = 0;

// rl.on("line", (line) => {
//   lines.push(line);
//   curLine++;
//   if (curLine === lineLimit) rl.close();
// }).on("close", () => {
//   const [n, m, k] = lines[0].split(" ").map((num) => parseInt(num));
//   const nums = lines[1].split(" ").map((num) => parseInt(num));

//   let biggestIdx = 0;
//   let nextIdx = 0;
//   let result = 0;

//   for (const [idx, num] of nums.entries()) {
//     if (num >= nums[biggestIdx]) {
//       nextIdx = biggestIdx;
//       biggestIdx = idx;
//     }
//   }

//   for (let i = 1; i <= m; i++) {
//     if (i % (k + 1) !== 0) {
//       result += nums[biggestIdx];
//     } else {
//       result += nums[nextIdx];
//     }
//   }

//   console.log(result);
// });

function solution(n, m, k, data) {
  let result = 0;
  let biggestIdx = 0;
  let nextIdx = 0;

  for (const [idx, num] of data.entries()) {
    if (num >= data[biggestIdx]) {
      nextIdx = biggestIdx;
      biggestIdx = idx;
    }
  }

  for (let i = 1; i <= m; i++) {
    if (i % (k + 1) !== 0) {
      result += data[biggestIdx];
    } else {
      result += data[nextIdx];
    }
  }

  return result;
}

module.exports = solution;
