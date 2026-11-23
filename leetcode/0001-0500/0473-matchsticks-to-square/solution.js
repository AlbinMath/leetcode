/**
 * @param {number[]} matchsticks
 * @return {boolean}
 */
var makesquare = function (matchsticks) {
  const total = matchsticks.reduce((a, b) => a + b, 0);
  if (total % 4 !== 0) return false;

  const side = total / 4;
  matchsticks.sort((a, b) => b - a);
  if (matchsticks[0] > side) return false;

  const sides = [0, 0, 0, 0];
  const n = matchsticks.length;

  const backtrack = (i) => {
    if (i === n) return true;

    const seen = new Set();
    for (let j = 0; j < 4; j++) {
      if (sides[j] + matchsticks[i] > side || seen.has(sides[j])) continue;

      seen.add(sides[j]);
      sides[j] += matchsticks[i];
      if (backtrack(i + 1)) return true;
      sides[j] -= matchsticks[i];
    }
    return false;
  };

  return backtrack(0);
};
