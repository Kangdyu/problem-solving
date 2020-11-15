// import readline from "readline";

// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });

// let n = 0;
// let coinCount = 0;

// const coins = [500, 100, 50, 10];

// rl.on("line", (line) => {
//   n = parseInt(line);
//   rl.close();
// }).on("close", () => {
//   for (const coin of coins) {
//     coinCount += Math.floor(n / coin);
//     n %= coin;
//   }

//   console.log(coinCount);
// });

function solution(n) {
  const coins = [500, 100, 50, 10];
  let coinCount = 0;

  for (const coin of coins) {
    coinCount += Math.floor(n / coin);
    n %= coin;
  }

  return coinCount;
}

module.exports = solution;
