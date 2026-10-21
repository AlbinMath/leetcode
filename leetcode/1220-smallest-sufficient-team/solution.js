/**
 * @param {string[]} req_skills
 * @param {string[][]} people
 * @return {number[]}
 */
var smallestSufficientTeam = function (req_skills, people) {
  const n = req_skills.length;
  const idx = new Map();
  req_skills.forEach((s, i) => idx.set(s, i));

  const full = (1 << n) - 1;
  const dp = new Array(1 << n).fill(null);
  dp[0] = [];

  for (let p = 0; p < people.length; p++) {
    let pm = 0;
    for (const s of people[p]) pm |= 1 << idx.get(s);
    if (pm === 0) continue;

    for (let mask = 0; mask <= full; mask++) {
      if (dp[mask] === null) continue;
      const nm = mask | pm;
      if (nm === mask) continue;
      if (dp[nm] === null || dp[mask].length + 1 < dp[nm].length) {
        dp[nm] = [...dp[mask], p];
      }
    }
  }

  return dp[full];
};
