function solution(n, k) {
  let result = 0;

  while (n !== 1) {
    if (n % k === 0) {
      n = Math.floor(n / k);
    } else {
      n--;
    }
    result++;
  }

  return result;
}

module.exports = solution;
