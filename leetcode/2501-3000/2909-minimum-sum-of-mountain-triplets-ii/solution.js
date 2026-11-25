var minimumSum = function(nums) {
    const n = nums.length;
    const leftMin = new Array(n);
    const rightMin = new Array(n);
    leftMin[0] = nums[0];
    for (let i = 1; i < n; i++) {
        leftMin[i] = Math.min(leftMin[i - 1], nums[i]);
    }
    rightMin[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        rightMin[i] = Math.min(rightMin[i + 1], nums[i]);
    }
    let ans = Infinity;
    for (let j = 1; j < n - 1; j++) {
        let left = leftMin[j - 1];
        let right = rightMin[j + 1];

        if (left < nums[j] && right < nums[j]) {
            let sum = left + nums[j] + right;
            ans = Math.min(ans, sum);
        }
    }
    return ans === Infinity ? -1 : ans;
};

