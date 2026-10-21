var numberWays = function (hats) {
  const MOD = 1000000007, n = hats.length, full = (1 << n) - 1;
  const byHat = Array.from({ length: 41 }, () => []);
  hats.forEach((list, p) => list.forEach((h) => byHat[h].push(p)));
  const dp = new Array(1 << n).fill(0);
  dp[0] = 1;
  for (let h = 1; h <= 40; h++) for (let m = full; m >= 0; m--) for (const p of byHat[h]) if (dp[m] && !(m & (1 << p))) dp[m | (1 << p)] = (dp[m | (1 << p)] + dp[m]) % MOD;
  return dp[full];
};
