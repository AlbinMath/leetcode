
var maxSum = function(nums, k) {
    const MOD = 1000000007n;
    const bits = new Array(31).fill(0);

    // Count set bits at each position
    for (const num of nums) {
        for (let b = 0; b < 31; b++) {
            if (Math.floor(num / (2 ** b)) % 2 === 1) {
                bits[b]++;
            }
        }
    }

    let ans = 0n;

    // Construct k maximum possible numbers
    for (let i = 0; i < k; i++) {
        let num = 0n;

        for (let b = 0; b < 31; b++) {
            if (bits[b] > 0) {
                num += 1n << BigInt(b);
                bits[b]--;
            }
        }

        ans = (ans + num * num) % MOD;
    }

    return Number(ans);
};

