
var getSumAbsoluteDifferences = function(nums) {
    const n = nums.length;
    const total = nums.reduce((sum, num) => sum + num, 0);

    let prefix = 0;
    let result = new Array(n);

    for (let i = 0; i < n; i++) {
        let left = i * nums[i] - prefix;

        let right = (total - prefix - nums[i]) 
                    - (n - i - 1) * nums[i];

        result[i] = left + right;

        prefix += nums[i];
    }

    return result;
};

