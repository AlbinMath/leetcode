
var minSwaps = function(nums, forbidden) {
    const n = nums.length;

    const numsFreq = new Map();
    const forbiddenFreq = new Map();
    const badFreq = new Map();

    let badCount = 0;
    let maxFreq = 0;

    // Step 1: Count frequencies
    for (let i = 0; i < n; i++) {
        numsFreq.set(nums[i], (numsFreq.get(nums[i]) || 0) + 1);

        forbiddenFreq.set(
            forbidden[i],
            (forbiddenFreq.get(forbidden[i]) || 0) + 1
        );
    }

    // Step 2: Check if a valid arrangement is possible
    for (let [num, count] of numsFreq) {
        const forbiddenCount = forbiddenFreq.get(num) || 0;

        if (count + forbiddenCount > n) {
            return -1;
        }
    }

    // Step 3: Count conflicting positions
    for (let i = 0; i < n; i++) {
        if (nums[i] === forbidden[i]) {
            badCount++;

            const count = (badFreq.get(nums[i]) || 0) + 1;

            badFreq.set(nums[i], count);

            maxFreq = Math.max(maxFreq, count);
        }
    }

    // Step 4: Calculate minimum swaps
    return Math.max(maxFreq, Math.ceil(badCount / 2));
};

