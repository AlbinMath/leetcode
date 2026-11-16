
var minArraySum = function(nums) {
    let maxVal = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }

    // 1. Mark which values exist in nums
    const present = new Uint8Array(maxVal + 1);
    for (let i = 0; i < nums.length; i++) {
        present[nums[i]] = 1;
    }

    // 2. For every value v, find the smallest present divisor in nums
    const minDiv = new Int32Array(maxVal + 1);
    for (let v = 1; v <= maxVal; v++) {
        minDiv[v] = v;
    }

    for (let d = 1; d <= maxVal; d++) {
        if (present[d]) {
            for (let multiple = d + d; multiple <= maxVal; multiple += d) {
                if (d < minDiv[multiple]) {
                    minDiv[multiple] = d;
                }
            }
        }
    }

    // 3. Replace each element with its smallest present divisor and sum
    let totalSum = 0;
    for (let i = 0; i < nums.length; i++) {
        totalSum += minDiv[nums[i]];
    }

    return totalSum;
};
