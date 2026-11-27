
var minSwaps = function(nums) {
    const even = [];
    const odd = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] % 2 === 0) {
            even.push(i);
        } else {
            odd.push(i);
        }
    }
    if (Math.abs(even.length - odd.length) > 1) {
        return -1;
    }
    function calculateCost(indices) {
        let swaps = 0;

        for (let i = 0; i < indices.length; i++) {
            swaps += Math.abs(indices[i] - 2 * i);
        }

        return swaps;
    }
    if (even.length > odd.length) {
        return calculateCost(even);
    }
    if (odd.length > even.length) {
        return calculateCost(odd);
    }
    return Math.min(
        calculateCost(even),
        calculateCost(odd)
    );
};

