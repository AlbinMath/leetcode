
var maxSum = function(nums) {
    const seen = new Set();
    let sum = 0;
    let maxValue = -Infinity;

    for (const num of nums) {
        maxValue = Math.max(maxValue, num);

        if (num > 0 && !seen.has(num)) {
            sum += num;
            seen.add(num);
        }
    }
    return sum > 0 ? sum : maxValue;
};

