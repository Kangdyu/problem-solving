function solution(n) {
  let result = 0;

  for (let i = 0; i <= n; i++) {
    if (i.toString().includes("3")) {
      result += 3600;
      continue;
    }
    for (let j = 0; j < 60; j++) {
      if (j.toString().includes("3")) {
        result += 60;
        continue;
      }
      for (let k = 0; k < 60; k++) {
        if (k.toString().includes("3")) {
          result += 1;
        }
      }
    }
  }

  return result;
}

module.exports = solution;
