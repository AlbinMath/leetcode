/**
 * @param {number[]} nums
 * @return {number}
 */
var countBeautifulPairs = function(nums) {
    // Helper function to compute Greatest Common Divisor
    const gcd = (a, b) => {
        while (b !== 0) {
            let temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    // Helper function to get the first digit of a positive integer
    const getFirstDigit = (num) => {
        while (num >= 10) {
            num = Math.floor(num / 10);
        }
        return num;
    };

    let count = 0;
    const n = nums.length;

    for (let i = 0; i < n; i++) {
        const firstDigit = getFirstDigit(nums[i]);
        for (let j = i + 1; j < n; j++) {
            const lastDigit = nums[j] % 10;
            if (gcd(firstDigit, lastDigit) === 1) {
                count++;
            }
        }
    }

    return count;
};
