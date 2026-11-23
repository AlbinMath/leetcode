
var getLength = function(nums) {
    const n = nums.length;
    let ans = 1;

    for (let i = 0; i < n; i++) {
        const freq = new Map();
        const freqCount = new Map();

        for (let j = i; j < n; j++) {
            const num = nums[j];

            const oldFreq = freq.get(num) || 0;
            const newFreq = oldFreq + 1;

            // Remove old frequency
            if (oldFreq > 0) {
                const count = freqCount.get(oldFreq);

                if (count === 1) {
                    freqCount.delete(oldFreq);
                } else {
                    freqCount.set(oldFreq, count - 1);
                }
            }

            // Update frequency
            freq.set(num, newFreq);

            freqCount.set(
                newFreq,
                (freqCount.get(newFreq) || 0) + 1
            );

            // Only one distinct value
            if (freq.size === 1) {
                ans = Math.max(ans, j - i + 1);
                continue;
            }

            // Check frequency balance
            if (freqCount.size === 2) {
                const [a, b] = freqCount.keys();

                if (Math.max(a, b) === 2 * Math.min(a, b)) {
                    ans = Math.max(ans, j - i + 1);
                }
            }
        }
    }

    return ans;
};

