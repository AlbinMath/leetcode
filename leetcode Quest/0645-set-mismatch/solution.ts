function findErrorNums(nums: number[]): number[] {
    const n = nums.length;
    const seen = new Set<number>();

    let duplicate = 0;

    for (const num of nums) {
        if (seen.has(num)) {
            duplicate = num;
        }
        seen.add(num);
    }

    let missing = 0;

    for (let i = 1; i <= n; i++) {
        if (!seen.has(i)) {
            missing = i;
            break;
        }
    }

    return [duplicate, missing];
}
