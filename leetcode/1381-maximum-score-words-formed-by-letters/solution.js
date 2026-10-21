/**
 * @param {string[]} words
 * @param {character[]} letters
 * @param {number[]} score
 * @return {number}
 */
var maxScoreWords = function (words, letters, score) {
  const avail = new Array(26).fill(0);
  for (const ch of letters) avail[ch.charCodeAt(0) - 97]++;

  const wordScore = words.map((w) => {
    let s = 0;
    for (const ch of w) s += score[ch.charCodeAt(0) - 97];
    return s;
  });

  const dfs = (i) => {
    if (i === words.length) return 0;

    // Option 1: skip this word
    let best = dfs(i + 1);

    // Option 2: use this word if letters allow
    let canUse = true;
    for (const ch of words[i]) {
      if (--avail[ch.charCodeAt(0) - 97] < 0) canUse = false;
    }
    if (canUse) best = Math.max(best, wordScore[i] + dfs(i + 1));

    // Restore letters
    for (const ch of words[i]) avail[ch.charCodeAt(0) - 97]++;

    return best;
  };

  return dfs(0);
};
