
var countOfPeaks = function(nums, queries) {
    const n = nums.length;
    const bit = new Array(n + 1).fill(0);

    function isPeak(i) {
        return i > 0 &&
               i < n - 1 &&
               nums[i] > nums[i - 1] &&
               nums[i] > nums[i + 1];
    }

    function update(i, delta) {
        for (i++; i <= n; i += i & -i) {
            bit[i] += delta;
        }
    }

    function query(i) {
        let sum = 0;

        for (i++; i > 0; i -= i & -i) {
            sum += bit[i];
        }

        return sum;
    }

    function rangeSum(left, right) {
        if (left > right) return 0;
        return query(right) - (left > 0 ? query(left - 1) : 0);
    }

    // Initialize peak indicators.
    for (let i = 1; i < n - 1; i++) {
        if (isPeak(i)) update(i, 1);
    }

    const answer = [];

    for (const [type, a, b] of queries) {
        if (type === 1) {
            // Endpoints of the queried subarray cannot be peaks.
            answer.push(rangeSum(a + 1, b - 1));
        } else {
            const index = a;
            const value = b;

            // Only these positions can change peak status.
            for (let i = Math.max(1, index - 1);
                 i <= Math.min(n - 2, index + 1);
                 i++) {
                if (isPeak(i)) update(i, -1);
            }

            nums[index] = value;

            for (let i = Math.max(1, index - 1);
                 i <= Math.min(n - 2, index + 1);
                 i++) {
                if (isPeak(i)) update(i, 1);
            }
        }
    }

    return answer;
};

