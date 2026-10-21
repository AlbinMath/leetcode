
var searchMatrix = function(matrix, target) {
    const rows = matrix.length;
    const cols = matrix[0].length;

    let row = 0;
    let col = cols - 1;

    while (row < rows && col >= 0) {
        const value = matrix[row][col];

        if (value === target) {
            return true;
        } else if (value > target) {
            // Current value is too large; move left
            col--;
        } else {
            // Current value is too small; move down
            row++;
        }
    }

    return false;
};

