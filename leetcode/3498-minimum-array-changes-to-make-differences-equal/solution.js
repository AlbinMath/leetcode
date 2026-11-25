
var minChanges = function(nums, k) {
    const n = nums.length;
    const changes = new Array(k + 2).fill(0);
    for (let i = 0; i < n / 2; i++) {
        const a = nums[i];
        const b = nums[n - 1 - i];

        const diff = Math.abs(a - b);
        const T = Math.max(a, b, k - a, k - b);
        changes[0] += 1;
        changes[T + 1] += 1;

        changes[diff] -= 1;
        changes[diff + 1] += 1;
    }

    let ans = Infinity;
    let current = 0;

    for (let x = 0; x <= k; x++) {
        current += changes[x];
        ans = Math.min(ans, current);
    }

    return ans;
};

