var matrixSum = function(nums) {
    const m = nums.length;
    const n = nums[0].length;

    // Sort each row in ascending order
    for (const row of nums) {
        row.sort((a, b) => a - b);
    }

    let score = 0;
    // Find the maximum in each column and add to score
    for (let j = 0; j < n; j++) {
        let colMax = 0;
        for (let i = 0; i < m; i++) {
            colMax = Math.max(colMax, nums[i][j]);
        }
        score += colMax;
    }

    return score;
};
