/**
 * @param {string[]} words
 * @return {string}
 */
var shortestSuperstring = function (words) {
  const n = words.length;
  const ov = (a, b) => {
    for (let l = Math.min(a.length, b.length) - 1; l > 0; l--)
      if (a.endsWith(b.slice(0, l))) return l;
    return 0;
  };
  const o = words.map((a) => words.map((b) => (a === b ? 0 : ov(a, b))));

  const size = 1 << n;
  const dp = Array.from({ length: size }, () => new Array(n).fill(-1));
  const par = Array.from({ length: size }, () => new Array(n).fill(-1));
  for (let i = 0; i < n; i++) dp[1 << i][i] = 0;

  for (let m = 1; m < size; m++)
    for (let l = 0; l < n; l++) {
      if (dp[m][l] < 0) continue;
      for (let x = 0; x < n; x++) {
        if (m & (1 << x)) continue;
        const nm = m | (1 << x);
        const v = dp[m][l] + o[l][x];
        if (v > dp[nm][x]) { dp[nm][x] = v; par[nm][x] = l; }
      }
    }

  let mask = size - 1, last = 0;
  for (let i = 1; i < n; i++) if (dp[mask][i] > dp[mask][last]) last = i;

  const order = [];
  while (last !== -1) {
    order.push(last);
    const p = par[mask][last];
    mask ^= 1 << last;
    last = p;
  }
  order.reverse();

  let res = words[order[0]];
  for (let k = 1; k < order.length; k++)
    res += words[order[k]].slice(o[order[k - 1]][order[k]]);
  return res;
};
