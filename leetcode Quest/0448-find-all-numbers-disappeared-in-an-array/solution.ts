function findDisappearedNumbers(nums: number[]): number[] {
    const result: number[] = [];

    // Mark the index corresponding to each number
    for (const num of nums) {
        const index = Math.abs(num) - 1;

        if (nums[index] > 0) {
            nums[index] = -nums[index];
        }
    }

    // Positive values mean the number is missing
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > 0) {
            result.push(i + 1);
        }
    }

    return result;
}
