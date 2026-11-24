/**
 * @param {number[][]} cost
 * @return {number}
 */
var connectTwoGroups = function (cost) {
  const n = cost.length;
  const m = cost[0].length;
  const size = 1 << m;

  const minCol = new Array(m).fill(Infinity);
  for (let i = 0; i < n; i++)
    for (let j = 0; j < m; j++) minCol[j] = Math.min(minCol[j], cost[i][j]);

  let dp = new Array(size).fill(Infinity);
  dp[0] = 0;

  for (let i = 0; i < n; i++) {
    const next = new Array(size).fill(Infinity);
    for (let mask = 0; mask < size; mask++) {
      if (dp[mask] === Infinity) continue;
      for (let j = 0; j < m; j++) {
        const nm = mask | (1 << j);
        next[nm] = Math.min(next[nm], dp[mask] + cost[i][j]);
      }
    }
    dp = next;
  }

  let ans = Infinity;
  for (let mask = 0; mask < size; mask++) {
    if (dp[mask] === Infinity) continue;
    let extra = 0;
    for (let j = 0; j < m; j++) {
      if (!(mask & (1 << j))) extra += minCol[j];
    }
    ans = Math.min(ans, dp[mask] + extra);
  }
  return ans;
};
