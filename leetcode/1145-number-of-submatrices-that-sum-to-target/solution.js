var numSubmatrixSumTarget = function(matrix, target) {
    const rows = matrix.length;
    const cols = matrix[0].length;
    let total = 0;

    for (let r1 = 0; r1 < rows; r1++) {
        const colSums = new Int32Array(cols);
        for (let r2 = r1; r2 < rows; r2++) {
            // Accumulate column sums for submatrices bounded by rows [r1, r2]
            for (let c = 0; c < cols; c++) {
                colSums[c] += matrix[r2][c];
            }

            // Count 1D subarrays in colSums that sum to target
            const prefixCounts = new Map();
            prefixCounts.set(0, 1);
            let currSum = 0;

            for (let c = 0; c < cols; c++) {
                currSum += colSums[c];
                total += prefixCounts.get(currSum - target) || 0;
                prefixCounts.set(currSum, (prefixCounts.get(currSum) || 0) + 1);
            }
        }
    }

    return total;
};
