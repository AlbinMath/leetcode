/**
 * @param {number[]} nums
 * @return {number}
 */
var maxScore = function(nums) {
    const n = nums.length;
    if (n === 1) return nums[0] * nums[0];

    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    const lcm = (a, b) => (a / gcd(a, b)) * b;

    const getScore = (skipIdx) => {
        let g = 0;
        let l = 1;

        for (let i = 0; i < n; i++) {
            if (i === skipIdx) continue;
            g = gcd(g, nums[i]);
            l = lcm(l, nums[i]);
        }

        return g * l;
    };

    // Baseline score without removing any element
    let best = getScore(-1);

    // Check score after removing each single element
    for (let i = 0; i < n; i++) {
        const score = getScore(i);
        if (score > best) {
            best = score;
        }
    }

    return best;
};
