/**
 * @param {number} n
 * @param {number[][]} relations
 * @param {number} k
 * @return {number}
 */
var minNumberOfSemesters = function (n, relations, k) {
  const pre = new Array(n).fill(0);
  for (const [a, b] of relations) pre[b - 1] |= 1 << (a - 1);

  const popcount = (x) => {
    let c = 0;
    for (; x; x &= x - 1) c++;
    return c;
  };

  const full = (1 << n) - 1;
  const dp = new Array(1 << n).fill(Infinity);
  dp[0] = 0;

  for (let mask = 0; mask < full; mask++) {
    if (dp[mask] === Infinity) continue;

    let avail = 0;
    for (let i = 0; i < n; i++) {
      if (!(mask & (1 << i)) && (pre[i] & mask) === pre[i]) avail |= 1 << i;
    }

    if (popcount(avail) <= k) {
      const nm = mask | avail;
      dp[nm] = Math.min(dp[nm], dp[mask] + 1);
    } else {
      for (let sub = avail; sub > 0; sub = (sub - 1) & avail) {
        if (popcount(sub) !== k) continue;
        const nm = mask | sub;
        dp[nm] = Math.min(dp[nm], dp[mask] + 1);
      }
    }
  }

  return dp[full];
};
