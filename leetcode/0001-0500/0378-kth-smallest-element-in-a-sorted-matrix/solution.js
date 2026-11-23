var kthSmallest = function(matrix, k) {
    const n = matrix.length;

    const countLessEqual = (target) => {
        let count = 0;
        let r = n - 1;
        let c = 0; // Start at bottom-left corner

        while (r >= 0 && c < n) {
            if (matrix[r][c] <= target) {
                // All elements in column c from row 0 to r are <= target
                count += r + 1;
                c++;
            } else {
                r--;
            }
        }
        return count;
    };

    let lo = matrix[0][0];
    let hi = matrix[n - 1][n - 1];

    while (lo < hi) {
        const mid = lo + Math.floor((hi - lo) / 2);
        if (countLessEqual(mid) < k) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }

    return lo;
};
