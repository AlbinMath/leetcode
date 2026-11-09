
var countOfPairs = function(n, x, y) {
    const result = new Array(n).fill(0);

    for (let i = 1; i <= n; i++) {
        for (let j = i + 1; j <= n; j++) {

            // Distance using the original straight road.
            const direct = j - i;

            // Distance using the additional road.
            const viaXY = Math.abs(i - x) + 1 + Math.abs(j - y);
            const viaYX = Math.abs(i - y) + 1 + Math.abs(j - x);

            // Minimum possible distance.
            const distance = Math.min(direct, viaXY, viaYX);

            // Count both ordered pairs: (i,j) and (j,i).
            result[distance - 1] += 2;
        }
    }

    return result;
};

