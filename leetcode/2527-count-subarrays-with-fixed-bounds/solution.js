/**
 * @param {number[]} nums
 * @param {number} minK
 * @param {number} maxK
 * @return {number}
 */
var countSubarrays = function (nums, minK, maxK) {
    let bad = -1, lastMin = -1, lastMax = -1;
    let ans = 0;

    for (let i = 0; i < nums.length; i++) {
        const x = nums[i];
        if (x < minK || x > maxK) bad = i;
        if (x === minK) lastMin = i;
        if (x === maxK) lastMax = i;
        ans += Math.max(0, Math.min(lastMin, lastMax) - bad);
    }
    return ans;
};

