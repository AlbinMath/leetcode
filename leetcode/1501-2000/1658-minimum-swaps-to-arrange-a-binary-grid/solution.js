
var minSwaps = function(grid) {
    const n = grid.length;
    const trailingZeros = new Array(n);

    // Count trailing zeros for each row
    for (let r = 0; r < n; r++) {
        let zeros = 0;
        for (let c = n - 1; c >= 0; c--) {
            if (grid[r][c] === 0) {
                zeros++;
            } else {
                break;
            }
        }
        trailingZeros[r] = zeros;
    }

    let swaps = 0;
    for (let i = 0; i < n; i++) {
        const required = n - 1 - i;
        // Find the nearest row at or below i with enough trailing zeros
        let j = i;
        while (j < n && trailingZeros[j] < required) {
            j++;
        }

        if (j === n) {
            return -1;
        }

        // Bubble row j up to position i using (j - i) adjacent swaps
        swaps += j - i;
        const chosen = trailingZeros[j];
        for (let k = j; k > i; k--) {
            trailingZeros[k] = trailingZeros[k - 1];
        }
        trailingZeros[i] = chosen;
    }

    return swaps;
};
