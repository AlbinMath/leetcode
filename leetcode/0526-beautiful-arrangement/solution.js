/**
 * @param {number} n
 * @return {number}
 */
var countArrangement = function (n) {
  const used = new Array(n + 1).fill(false);
  let count = 0;

  const backtrack = (pos) => {
    if (pos === 0) {
      count++;
      return;
    }
    for (let num = 1; num <= n; num++) {
      if (used[num]) continue;
      if (num % pos !== 0 && pos % num !== 0) continue;

      used[num] = true;
      backtrack(pos - 1);
      used[num] = false;
    }
  };

  backtrack(n);
  return count;
};
