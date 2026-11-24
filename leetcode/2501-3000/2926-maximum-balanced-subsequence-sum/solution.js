
var maxBalancedSubsequenceSum = function(nums) {
    const n = nums.length;
    const values = nums.map((x, i) => x - i);
    const sorted = [...new Set(values)].sort((a, b) => a - b);
    const m = sorted.length;

    const bit = new Array(m + 1).fill(-Infinity);

    function getRank(target) {
        let left = 0;
        let right = m - 1;

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);

            if (sorted[mid] === target) {
                return mid + 1;
            } else if (sorted[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return left + 1;
    }

    function query(i) {
        let best = -Infinity;

        while (i > 0) {
            best = Math.max(best, bit[i]);
            i -= i & -i;
        }

        return best;
    }

    function update(i, value) {
        while (i <= m) {
            bit[i] = Math.max(bit[i], value);
            i += i & -i;
        }
    }

    let answer = -Infinity;

    for (let i = 0; i < n; i++) {
        const rank = getRank(nums[i] - i);
        const bestPrevious = query(rank);
        const current = Math.max(nums[i], nums[i] + bestPrevious);

        update(rank, current);
        answer = Math.max(answer, current);
    }

    return answer;
};

