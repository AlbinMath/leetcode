var kthSmallestPath = function(destination, k) {
    let [row, col] = destination;
    let result = "";

    while (row > 0 || col > 0) {
        if (col === 0) {
            result += "V";
            row--;
            continue;
        }

        if (row === 0) {
            result += "H";
            col--;
            continue;
        }

        // Number of paths starting with H
        let count = 1;
        for (let i = 1; i <= row; i++) {
            count = count * (col + row - i) / i;
        }

        if (k <= count) {
            result += "H";
            col--;
        } else {
            result += "V";
            k -= count;
            row--;
        }
    }

    return result;
};
