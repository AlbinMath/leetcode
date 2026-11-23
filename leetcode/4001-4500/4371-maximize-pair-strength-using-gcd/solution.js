/**
 * @param {number[]} nums
 * @return {number}
 */
var maxPairStrength = function(nums) {
    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    // Sort descending to enable early pruning when nums[i] * nums[j] <= maxStrength
    nums.sort((a, b) => b - a);

    const n = nums.length;
    let maxStrength = 0;

    for (let i = 0; i < n - 1; i++) {
        const a = nums[i];
        // Even with gcd = 1, no remaining pair with a can beat maxStrength
        if (a * nums[i + 1] <= maxStrength) break;

        for (let j = i + 1; j < n; j++) {
            const b = nums[j];
            if (a * b <= maxStrength) break;

            const g = gcd(a, b);
            const strength = (a / g) * (b / g);
            if (strength > maxStrength) {
                maxStrength = strength;
            }
        }
    }

    return maxStrength;
};
