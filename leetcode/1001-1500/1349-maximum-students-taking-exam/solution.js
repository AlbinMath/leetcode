/**
 * @param {character[][]} seats
 * @return {number}
 */
var maxStudents = function (seats) {
  const m = seats.length;
  const n = seats[0].length;
  const size = 1 << n;

  const popcount = (x) => {
    let c = 0;
    for (; x; x &= x - 1) c++;
    return c;
  };

  // broken[r] has a bit set for each broken seat in row r
  const broken = seats.map((row) => {
    let b = 0;
    for (let c = 0; c < n; c++) if (row[c] === "#") b |= 1 << c;
    return b;
  });

  let dp = new Array(size).fill(-1);
  dp[0] = 0; // virtual empty row above row 0

  for (let r = 0; r < m; r++) {
    const next = new Array(size).fill(-1);
    for (let cur = 0; cur < size; cur++) {
      if (cur & broken[r]) continue;
      if (cur & (cur >> 1)) continue;
      const cnt = popcount(cur);
      for (let prev = 0; prev < size; prev++) {
        if (dp[prev] < 0) continue;
        if (cur & (prev << 1) || cur & (prev >> 1)) continue;
        next[cur] = Math.max(next[cur], dp[prev] + cnt);
      }
    }
    dp = next;
  }

  return Math.max(...dp);
};
