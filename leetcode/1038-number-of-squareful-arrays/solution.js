/**
 * @param {number[]} nums
 * @return {number}
 */
var numSquarefulPerms = function (nums) {
  nums.sort((a, b) => a - b);
  const n = nums.length;

  const isSquare = (x) => {
    const r = Math.round(Math.sqrt(x));
    return r * r === x;
  };

  const ok = Array.from({ length: n }, () => new Array(n).fill(false));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (i !== j) ok[i][j] = isSquare(nums[i] + nums[j]);
    }
  }

  const used = new Array(n).fill(false);
  let count = 0;

  const dfs = (depth, prev) => {
    if (depth === n) {
      count++;
      return;
    }
    for (let i = 0; i < n; i++) {
      if (used[i]) continue;
      if (i > 0 && nums[i] === nums[i - 1] && !used[i - 1]) continue;
      if (prev !== -1 && !ok[prev][i]) continue;

      used[i] = true;
      dfs(depth + 1, i);
      used[i] = false;
    }
  };

  dfs(0, -1);
  return count;
};
