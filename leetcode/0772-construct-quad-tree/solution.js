
var construct = function(grid) {
    const n = grid.length;

    function build(row, col, size) {
        const value = grid[row][col];
        let uniform = true;

        // Check whether this region contains only one value
        for (let r = row; r < row + size; r++) {
            for (let c = col; c < col + size; c++) {
                if (grid[r][c] !== value) {
                    uniform = false;
                    break;
                }
            }

            if (!uniform) break;
        }

        // A uniform region becomes a leaf
        if (uniform) {
            return new Node(value === 1, true);
        }

        const half = size / 2;

        // Divide into four quadrants
        const topLeft = build(row, col, half);
        const topRight = build(row, col + half, half);
        const bottomLeft = build(row + half, col, half);
        const bottomRight = build(
            row + half,
            col + half,
            half
        );

        return new Node(
            true,
            false,
            topLeft,
            topRight,
            bottomLeft,
            bottomRight
        );
    }

    return build(0, 0, n);
};

