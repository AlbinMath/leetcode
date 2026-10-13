
var numIslands = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    let islands = 0;

    function dfs(row, col) {
        // Stop if outside the grid or on water
        if (
            row < 0 ||
            row >= m ||
            col < 0 ||
            col >= n ||
            grid[row][col] === "0"
        ) {
            return;
        }

        // Mark this land cell as visited
        grid[row][col] = "0";

        // Explore all four directions
        dfs(row - 1, col); // Up
        dfs(row + 1, col); // Down
        dfs(row, col - 1); // Left
        dfs(row, col + 1); // Right
    }

    for (let row = 0; row < m; row++) {
        for (let col = 0; col < n; col++) {
            if (grid[row][col] === "1") {
                islands++;
                dfs(row, col);
            }
        }
    }

    return islands;
};

