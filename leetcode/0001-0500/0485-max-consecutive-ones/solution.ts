function findMaxConsecutiveOnes(nums: number[]): number {
    let current = 0;
    let max = 0;

    for (const num of nums) {
        if (num === 1) {
            current++;
            max = Math.max(max, current);
        } else {
            current = 0;
        }
    }

    return max;
}
