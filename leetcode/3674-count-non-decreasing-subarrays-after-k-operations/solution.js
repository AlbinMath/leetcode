/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countNonDecreasingSubarrays = function (nums, k) {
    const n = nums.length;
    const pre = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pre[i + 1] = pre[i] + nums[i];

    const st = new Array(n); // chain stack: top (smallest index) is st[sz-1], bottom is st[bot]
    let bot = 0, sz = 0;
    let total = 0;          // sum of nums[c] * segment length
    let r = n - 1;
    let ans = 0;

    for (let l = n - 1; l >= 0; l--) {
        // pop chain elements that l now dominates
        while (sz > bot && nums[st[sz - 1]] <= nums[l]) {
            const c = st[sz - 1];
            const end = (sz - 1 > bot) ? st[sz - 2] : r + 1; // exclusive end of c's segment
            total -= nums[c] * (end - c);
            sz--;
        }
        // push l; its segment ends before the next chain element (or at r)
        const end = (sz > bot) ? st[sz - 1] : r + 1;
        total += nums[l] * (end - l);
        st[sz++] = l;

        // shrink r while cost exceeds k
        while (total - (pre[r + 1] - pre[l]) > k) {
            const c = st[bot];
            total -= nums[c];
            if (c === r) bot++;
            r--;
        }
        ans += r - l + 1;
    }
    return ans;
};
