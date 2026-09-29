function smallerNumbersThanCurrent(nums: number[]): number[] {
    const count = new Array(101).fill(0);

    // Count frequency of each number
    for (const num of nums) {
        count[num]++;
    }

    // Prefix sum: count[x] = numbers <= x
    for (let i = 1; i <= 100; i++) {
        count[i] += count[i - 1];
    }

    const result: number[] = [];

    for (const num of nums) {
        // Number of elements strictly smaller than num
        result.push(num === 0 ? 0 : count[num - 1]);
    }

    return result;
}
