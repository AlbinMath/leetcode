
var maximumTripletValue = function(nums) {
    let ans = 0;
    const n = nums.length;

    for (let i = 0; i < n - 2; i++) {
        for (let j = i + 1; j < n - 1; j++) {
            for (let k = j + 1; k < n; k++) {
                let value = (nums[i] - nums[j]) * nums[k];

                ans = Math.max(ans, value);
            }
        }
    }

    return ans;
};

