
var minimumIndex = function(nums) {
    const n = nums.length;
    const freq = new Map();

    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    let dominant = -1;
    let totalCount = 0;

    for (const [num, count] of freq) {
        if (count * 2 > n) {
            dominant = num;
            totalCount = count;
            break;
        }
    }

    let leftCount = 0;

    for (let i = 0; i < n - 1; i++) {
        if (nums[i] === dominant) {
            leftCount++;
        }

        const leftLength = i + 1;
        const rightLength = n - leftLength;
        const rightCount = totalCount - leftCount;

        if (
            leftCount * 2 > leftLength &&
            rightCount * 2 > rightLength
        ) {
            return i;
        }
    }

    return -1;
};

