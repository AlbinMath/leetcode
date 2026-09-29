Array.prototype.snail = function(
    rowsCount: number,
    colsCount: number
): number[][] {
    const nums = this;

    if (rowsCount * colsCount !== nums.length) {
        return [];
    }

    const result: number[][] = Array.from(
        { length: rowsCount },
        () => Array(colsCount)
    );

    let index = 0;

    for (let col = 0; col < colsCount; col++) {
        if (col % 2 === 0) {
            // Top → Bottom
            for (let row = 0; row < rowsCount; row++) {
                result[row][col] = nums[index++];
            }
        } else {
            // Bottom → Top
            for (let row = rowsCount - 1; row >= 0; row--) {
                result[row][col] = nums[index++];
            }
        }
    }

    return result;
};
