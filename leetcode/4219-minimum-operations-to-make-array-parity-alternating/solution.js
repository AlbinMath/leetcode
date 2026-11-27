var makeParityAlternating = function(nums) {
    const n = nums.length;

    if (n === 1) return [0, 0];

    function getCost(startParity) {
        let cost = 0;

        for (let i = 0; i < n; i++) {
            const parity = ((nums[i] % 2) + 2) % 2;
            const required = (startParity + i) % 2;

            if (parity !== required) cost++;
        }

        return cost;
    }

    const costEvenStart = getCost(0);
    const costOddStart = getCost(1);
    const minOps = Math.min(costEvenStart, costOddStart);

    function getMinRange(startParity) {
        const candidates = [];

        for (let i = 0; i < n; i++) {
            const parity = ((nums[i] % 2) + 2) % 2;
            const required = (startParity + i) % 2;

            if (parity === required) {
                candidates.push([nums[i], i]);
            } else {
                candidates.push([nums[i] - 1, i]);
                candidates.push([nums[i] + 1, i]);
            }
        }

        candidates.sort((a, b) => a[0] - b[0]);

        const count = new Array(n).fill(0);
        let covered = 0;
        let left = 0;
        let minRange = Infinity;

        for (let right = 0; right < candidates.length; right++) {
            const index = candidates[right][1];

            if (count[index] === 0) covered++;
            count[index]++;

            while (covered === n) {
                minRange = Math.min(
                    minRange,
                    candidates[right][0] - candidates[left][0]
                );

                const leftIndex = candidates[left][1];
                count[leftIndex]--;

                if (count[leftIndex] === 0) covered--;

                left++;
            }
        }

        return minRange;
    }

    let minRange = Infinity;

    if (costEvenStart === minOps) {
        minRange = Math.min(minRange, getMinRange(0));
    }

    if (costOddStart === minOps) {
        minRange = Math.min(minRange, getMinRange(1));
    }

    return [minOps, minRange];
};
