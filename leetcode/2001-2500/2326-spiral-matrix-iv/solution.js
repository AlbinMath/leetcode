
var spiralMatrix = function(m, n, head) {
    // Step 1: Initialize matrix with -1
    let matrix = Array.from(
        { length: m },
        () => Array(n).fill(-1)
    );

    // Step 2: Initialize boundaries
    let top = 0;
    let bottom = m - 1;
    let left = 0;
    let right = n - 1;

    let current = head;

    // Step 3: Fill matrix in spiral order
    while (current && top <= bottom && left <= right) {

        // Move right
        for (let col = left; col <= right && current; col++) {
            matrix[top][col] = current.val;
            current = current.next;
        }
        top++;

        // Move down
        for (let row = top; row <= bottom && current; row++) {
            matrix[row][right] = current.val;
            current = current.next;
        }
        right--;

        // Move left
        for (let col = right; col >= left && current; col--) {
            matrix[bottom][col] = current.val;
            current = current.next;
        }
        bottom--;

        // Move up
        for (let row = bottom; row >= top && current; row--) {
            matrix[row][left] = current.val;
            current = current.next;
        }
        left++;
    }

    return matrix;
};

