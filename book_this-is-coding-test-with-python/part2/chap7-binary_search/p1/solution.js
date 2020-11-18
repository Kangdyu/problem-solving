const my = [8, 3, 7, 9, 2];
const ask = [5, 7, 9];

function binarySearch(target, array) {
  let start = 0;
  let end = array.length;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);

    if (target === array[mid]) return true;
    else if (target < array[mid]) end = mid - 1;
    else if (target > array[mid]) start = mid + 1;
  }

  return false;
}

function solutionOne(my, ask) {
  my.sort((a, b) => a - b);

  for (const i of ask) {
    if (binarySearch(i, my)) console.log("yes ");
    else console.log("no ");
  }
}

function solutionTwo(my, ask) {
  let container = new Array(my.length).fill(0);

  for (const i of my) {
    container[i] = 1;
  }

  for (const i of ask) {
    if (container[i] === 1) console.log("yes ");
    else console.log("no ");
  }
}

function solutionThree(my, ask) {
  const set = new Set(my);

  for (const i of ask) {
    if (set.has(i)) console.log("yes ");
    else console.log("no ");
  }
}

console.log("=== binary search ===");
solutionOne(my, ask);
console.log("=== counting sort ===");
solutionTwo(my, ask);
console.log("=== set ===");
solutionThree(my, ask);
