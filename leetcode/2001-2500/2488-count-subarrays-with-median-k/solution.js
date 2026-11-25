var countSubarrays = function(nums, k) {
    const n = nums.length;
    const pos = nums.indexOf(k);
    let count = new Map();
    count.set(0, 1);
    let balance = 0;
    for (let i = pos + 1; i < n; i++) {
        if (nums[i] > k) {
            balance++;
        } else {
            balance--;
        }
        count.set(balance, (count.get(balance) || 0) + 1);
    }
    let ans = 0;
    balance = 0;
    for (let i = pos; i >= 0; i--) {
        if (i < pos) {
            if (nums[i] > k) {
                balance++;
            } else {
                balance--;
            }
        }
        ans += count.get(-balance) || 0;
        ans += count.get(1 - balance) || 0;
    }
    return ans;
};

