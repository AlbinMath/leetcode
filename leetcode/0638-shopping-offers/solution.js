/**
 * @param {number[]} price
 * @param {number[][]} special
 * @param {number[]} needs
 * @return {number}
 */
var shoppingOffers = function (price, special, needs) {
  const n = price.length;
  const memo = new Map();

  // Drop offers that cost more than buying their items individually
  const offers = special.filter((s) => {
    let regular = 0;
    for (let i = 0; i < n; i++) regular += s[i] * price[i];
    return s[n] < regular;
  });

  const dfs = (cur) => {
    const key = cur.join(",");
    if (memo.has(key)) return memo.get(key);

    // Baseline: buy everything at full price
    let best = 0;
    for (let i = 0; i < n; i++) best += cur[i] * price[i];

    for (const offer of offers) {
      const next = new Array(n);
      let valid = true;
      for (let i = 0; i < n; i++) {
        next[i] = cur[i] - offer[i];
        if (next[i] < 0) {
          valid = false;
          break;
        }
      }
      if (valid) best = Math.min(best, offer[n] + dfs(next));
    }

    memo.set(key, best);
    return best;
  };

  return dfs(needs);
};
