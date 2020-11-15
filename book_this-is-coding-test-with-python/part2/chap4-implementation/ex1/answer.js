let coords = {
  x: 1,
  y: 1,

  left: function () {
    if (this.x !== 1) this.x -= 1;
  },
  right: function () {
    if (this.x !== this.maxX) this.x += 1;
  },
  up: function () {
    if (this.y !== 1) this.y -= 1;
  },
  down: function () {
    if (this.y !== this.maxY) this.y += 1;
  },
};

function solution(n, commands) {
  coords.maxX = n;
  coords.maxY = n;

  for (const command of commands) {
    if (command === "L") coords.left();
    else if (command === "R") coords.right();
    else if (command === "U") coords.up();
    else if (command === "D") coords.down();
  }

  return { x: coords.x, y: coords.y };
}

module.exports = solution;
