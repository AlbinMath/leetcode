/**
 * @param {number[]} nums
 * @return {number}
 */
var maxLength = function(nums) {
    const n = nums.length;
    // Max possible lcm(1..10) * max possible gcd(1..10) = 2520 * 10
    const MAX_PRODUCT = 25200;

    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    const lcm = (a, b) => (a / gcd(a, b)) * b;

    let maxLen = 1;

    for (let i = 0; i < n; i++) {
        let prod = 1;
        let g = 0;
        let l = 1;

        for (let j = i; j < n; j++) {
            const val = nums[j];
            prod *= val;
            if (prod > MAX_PRODUCT) break;

            g = gcd(g, val);
            l = lcm(l, val);

            if (prod === l * g) {
                maxLen = Math.max(maxLen, j - i + 1);
            }
        }
    }

    return maxLen;
};
