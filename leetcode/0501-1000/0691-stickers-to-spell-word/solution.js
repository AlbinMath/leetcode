/**
 * @param {string[]} stickers
 * @param {string} target
 * @return {number}
 */
var minStickers = function (stickers, target) {
  const m = target.length;
  const full = (1 << m) - 1;

  const counts = stickers.map((s) => {
    const c = new Array(26).fill(0);
    for (const ch of s) c[ch.charCodeAt(0) - 97]++;
    return c;
  });

  const dp = new Array(1 << m).fill(Infinity);
  dp[0] = 0;

  for (let mask = 0; mask < full; mask++) {
    if (dp[mask] === Infinity) continue;

    let p = 0;
    while (mask & (1 << p)) p++;
    const need = target.charCodeAt(p) - 97;

    for (const cnt of counts) {
      if (cnt[need] === 0) continue;

      const left = cnt.slice();
      let next = mask;
      for (let i = 0; i < m; i++) {
        if (next & (1 << i)) continue;
        const c = target.charCodeAt(i) - 97;
        if (left[c] > 0) {
          left[c]--;
          next |= 1 << i;
        }
      }
      if (dp[mask] + 1 < dp[next]) dp[next] = dp[mask] + 1;
    }
  }

  return dp[full] === Infinity ? -1 : dp[full];
};
