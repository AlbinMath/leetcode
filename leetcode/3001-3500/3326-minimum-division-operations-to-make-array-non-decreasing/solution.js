/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    // Helper to find the smallest prime factor of x (for x > 1)
    const getSmallestPrimeFactor = (x) => {
        if (x % 2 === 0) return 2;
        for (let d = 3; d * d <= x; d += 2) {
            if (x % d === 0) return d;
        }
        return x; // x is prime
    };

    let operations = 0;

    // Traverse from right to left so each element is bounded by its right neighbor
    for (let i = nums.length - 2; i >= 0; i--) {
        if (nums[i] > nums[i + 1]) {
            nums[i] = getSmallestPrimeFactor(nums[i]);
            operations++;

            // If even its smallest prime factor is greater than nums[i + 1], it's impossible
            if (nums[i] > nums[i + 1]) {
                return -1;
            }
        }
    }

    return operations;
};
