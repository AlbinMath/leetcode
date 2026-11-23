/**
 * @param {number[]} nums
 * @return {number}
 */
var continuousSubarrays = function (nums) {
    const n = nums.length;
    const maxQ = new Array(n), minQ = new Array(n);
    let maxH = 0, maxT = 0, minH = 0, minT = 0;
    let l = 0, ans = 0;

    for (let r = 0; r < n; r++) {
        while (maxH < maxT && nums[maxQ[maxT - 1]] <= nums[r]) maxT--;
        maxQ[maxT++] = r;
        while (minH < minT && nums[minQ[minT - 1]] >= nums[r]) minT--;
        minQ[minT++] = r;

        while (nums[maxQ[maxH]] - nums[minQ[minH]] > 2) {
            l++;
            if (maxQ[maxH] < l) maxH++;
            if (minQ[minH] < l) minH++;
        }
        ans += r - l + 1;
    }
    return ans;
};
