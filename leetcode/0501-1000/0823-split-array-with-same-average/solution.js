/**
 * @param {number[]} nums
 * @return {boolean}
 */
var splitArraySameAverage = function (nums) {
  const n = nums.length;
  if (n === 1) return false;

  const S = nums.reduce((a, b) => a + b, 0);
  const half = Math.floor(n / 2);

  let possible = false;
  for (let k = 1; k <= half; k++) {
    if ((S * k) % n === 0) {
      possible = true;
      break;
    }
  }
  if (!possible) return false;

  const dp = Array.from({ length: half + 1 }, () => new Set());
  dp[0].add(0);

  for (const num of nums) {
    for (let k = half; k >= 1; k--) {
      for (const s of dp[k - 1]) {
        dp[k].add(s + num);
      }
    }
  }

  for (let k = 1; k <= half; k++) {
    if ((S * k) % n === 0 && dp[k].has((S * k) / n)) return true;
  }
  return false;
};
