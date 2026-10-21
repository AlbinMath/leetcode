/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var canPartitionKSubsets = function (nums, k) {
  const total = nums.reduce((a, b) => a + b, 0);
  if (total % k !== 0) return false;

  const target = total / k;
  if (Math.max(...nums) > target) return false;

  const n = nums.length;
  const full = (1 << n) - 1;
  const dp = new Array(1 << n).fill(-1);
  dp[0] = 0;

  for (let mask = 0; mask < full; mask++) {
    if (dp[mask] === -1) continue;
    for (let i = 0; i < n; i++) {
      if (mask & (1 << i)) continue;
      if (dp[mask] + nums[i] > target) continue;
      dp[mask | (1 << i)] = (dp[mask] + nums[i]) % target;
    }
  }

  return dp[full] === 0;
};
