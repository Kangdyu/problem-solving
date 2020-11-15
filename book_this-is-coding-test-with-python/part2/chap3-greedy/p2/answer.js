// import readline from "readline";

// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });

// let lines = [];
// let lineLimit = 0;
// let curLine = 0;

// rl.on("line", (line) => {
//   lines.push(line);

//   if (curLine === 0) {
//     lineLimit = +line.split(" ")[0] + 1;
//   }

//   curLine++;
//   if (curLine === lineLimit) {
//     rl.close();
//   }
// }).on("close", () => {
//   let data = [];
//   for (let i = 1; i <= lineLimit - 1; i++) {
//     data.push(lines[i].split(" ").map((num) => parseInt(num)));
//   }

//   let result = 0;
//   for (const row of data) {
//     const minValue = Math.min(...row);
//     if (minValue > result) result = minValue;
//   }

//   console.log(result);
// });

function solution(n, m, data) {
  let result = 0;
  for (const row of data) {
    const minValue = Math.min(...row);
    if (minValue > result) result = minValue;
  }

  return result;
}

module.exports = solution;
