
/**
 * @param {number[]} nums
 * @param {number} goal
 * @return {number}
 */
var minAbsDifference = function(nums, goal) {
    const n = nums.length;
    const mid = Math.floor(n / 2);

    // Generate every possible subset sum for an array.
    function getSubsetSums(arr) {
        const sums = [0];

        for (const num of arr) {
            const size = sums.length;

            for (let i = 0; i < size; i++) {
                sums.push(sums[i] + num);
            }
        }

        return sums;
    }

    const leftSums = getSubsetSums(nums.slice(0, mid));
    const rightSums = getSubsetSums(nums.slice(mid));

    // Sort one half to enable binary search.
    rightSums.sort((a, b) => a - b);

    let answer = Math.abs(goal);

    for (const leftSum of leftSums) {
        if (answer === 0) return 0;

        const target = goal - leftSum;

        // Find the first rightSum >= target.
        let low = 0;
        let high = rightSums.length;

        while (low < high) {
            const m = Math.floor((low + high) / 2);

            if (rightSums[m] < target) {
                low = m + 1;
            } else {
                high = m;
            }
        }

        // Check the first sum >= target.
        if (low < rightSums.length) {
            answer = Math.min(
                answer,
                Math.abs(leftSum + rightSums[low] - goal)
            );
        }

        // Also check the closest sum below target.
        if (low > 0) {
            answer = Math.min(
                answer,
                Math.abs(leftSum + rightSums[low - 1] - goal)
            );
        }
    }

    return answer;
};

